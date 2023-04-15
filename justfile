#!/usr/bin/env just --justfile
name := "wrap_gptj4all"
module := "wrap_gptj4all"
description := """
A wrapper around gpt4all-j
"""
version := "0.0.1"
git_head := `git rev-list --max-parents=0 HEAD`
set allow-duplicate-recipes

# Don't let your dreams be dreams
doit: build run test
# default help text
@help:
    just --list --unsorted --list-prefix '|   ' --list-heading $'{{description}}\n{{name}} {{version}}:\n'
# Build
@build:
  true
# Run
@run:
  python3 -m {{module}}
test *args='':
  #!/usr/bin/env bash
  pytest {{ args }}
  if [ $? -eq 0 ]; then
    if ! [ -f build/.pass ]; then
      read -p "Pass commit comment: " COMMENT
      just _git_push_pass "${COMMENT}"
      rm build/.fail || true
      touch build/.pass
    fi
  else
    if ! [ -f build/.fail ]; then
      read -p "Fail commit comment: " COMMENT
      just _git_push_fail "${COMMENT}"
      rm build/.pass || true
      touch build/.fail
    fi
  fi
# Select an option from the menu
from_menu: _check_os
  #!/usr/bin/env bash
  just --choose

# Create developer directories
@create_dev_dirs:
    mkdir -p build/state
    [ -f .gitignore ] || echo "build" > .gitignore
# Clean temporary files
@clean state="*": (clean_state state)
# Clean temporary state files
@clean_state state="*":
    rm build/state/_{{state}}
# recipe to create a state file if the provided rule passes and not run the rule if a statefile already exists
@_once name *args="": create_dev_dirs
    [ -f build/state/{{name}} ] || ( just {{name}} {{args}} && date "+%Y-%m-%d %H:%M:%S" > build/state/{{name}} )
# Get information about the state of the build
@get_state:
    grep -r . build/state | sed 's/[^_]*_\([^:]*\):\(.*\)/\2 \1/' | sort -n
# Install developer dependencies
@dev_install_deps: (_once "_dev_install_deps" "")
@_dev_install_deps:
    ./dev_install_deps.sh
# Create poetry project
@create_poetry_project: (_once "_create_poetry_project" "")
@_create_poetry_project project="poetry_project":
    poetry init
# Add poetry dependency
@add_dep dep="":
    poetry add {{dep}}
# Install runtime deps
@install_deps: (_once "_install_deps" "")
@_install_deps:
    ./install_deps.sh
# Run the thing
ins_runtall_deps: (_once "_download" "")
@_ins_runtall_deps:
	@poetry run python -m gpt4all_voice
# Download stuff
@download: (_once "_download" "")
@_download:
    ./download.sh
#source .venv/bin/activate
#python -m gpt4all
# clean:
# 	@rm `git ls-files -i -o --exclude-standard`

auto_rebase: _commit_squash_warnings
  git rebase -i --autosquash {{ git_head }}
_commit_squash_warnings:
  git log --pretty='format:%h %s' | awk '{if ( $2 == ":warning:" ) { print "git commit --fixup "$1 }}' | sh || true
# Push all updates to git
_git_push comment="update" *args="":
  git add -A
  git commit -m "{{ comment }}" {{ args }}
  git push
# manual push :see_no_evil: :hear_no_evil: :speak_no_evil: :pray:
git_push comment="And I did not write a comment :cry:" *args="":
  just _git_push ":see_no_evil: I did not test this. {{ comment }}" {{ args }}
# push on fail
_git_push_fail *args="The test failed, and I did not write a comment :cry:":
  just _git_push ":warning: {{ args }}"
# push on pass
_git_push_pass *args="The test passed, but I did not write a comment :cry:": && auto_rebase
  just _git_push ":white_check_mark: {{ args }}"

[macos]
@_check_os:
[linux]
@_check_os:
  echo "Linux not tested" && exit 1
[windows]
@_check_os:
  echo "Windows not tested" && exit 1