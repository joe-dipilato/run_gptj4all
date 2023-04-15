run:
	@poetry run python -m gpt4all_voice
build_dependencies: runtime_deps
	@./build_dependencies.sh
runtime_deps:
	@./runtime_deps.sh
download_gpt4all:
	@./download_gpt4all.sh
project_config:
	@./_project_config.sh
# clean:
# 	@rm `git ls-files -i -o --exclude-standard`