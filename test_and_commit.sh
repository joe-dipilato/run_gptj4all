#!/usr/bin/env bash
mv build/latest.xml build/current.xml > /dev/null 2>&1 || true
mv build/current.xml build/latest.xml
pytest --junit-xml=build/current.xml $@
result=$?
message=$(python3 tools/parse_junit.py)
echo $message
if [ ${result} -eq 0 ]; then
  echo "Tests passed"
  if ! [ -f build/.pass ]; then
    message=$(python3 tools/parse_junit.py)
    echo $message
    read -p "Pass commit comment: [Enter to accept]" COMMENT
    just _git_push_pass "${COMMENT} ${message}"
    rm build/.fail || true
    touch build/.pass
    mv build/latest.xml build/previous.xml
  fi
else
  echo "Tests failed"
  if ! [ -f build/.fail ]; then
    message=$(python3 tools/parse_junit.py)
    echo $message
    read -p "Fail commit comment [Enter to accept]: " COMMENT
    just _git_push_fail "${COMMENT} ${message}"
    rm build/.pass || true
    touch build/.fail
    mv build/latest.xml build/previous.xml
  fi
fi
echo $message
rm build/latest.xml > /dev/null 2>&1 || true
