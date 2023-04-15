from junitparser import JUnitXml
from pathlib import Path
import sys

if not Path('build/previous.xml').exists():
    sys.exit(0)

if not Path('build/current.xml').exists():
    raise(Exception("Current test results do not exist"))

xml_prev = JUnitXml.fromfile(Path('build/previous.xml'))
xml_curr = JUnitXml.fromfile(Path('build/current.xml'))

# Determine which tests have different results in the current and previous test runs
# use comprehension to get a list of tuples of test names and results
# note that xml_prev and xml_curr iterate through testsuites of testcases
# first we get the testsuites

prev_test = {test_case.name:test_case.is_passed for test_suite in xml_prev for test_case in test_suite}
curr_test = {test_case.name:test_case.is_passed for test_suite in xml_curr for test_case in test_suite}
all_tests = set(prev_test.keys()).union(set(curr_test.keys()))
curr_tests = set(curr_test.keys())
prev_tests = set(prev_test.keys())
existing_test = prev_tests.intersection(curr_tests)
added_test =  curr_tests.difference(prev_tests)
removed_test = prev_tests.difference(curr_tests)
changed_test = set(name for name in existing_test if curr_test[name] != prev_test[name])
new_pass = set(name for name in changed_test if curr_test[name] == True)
new_fail = set(name for name in changed_test if curr_test[name] == False)

result =""
if added_test:
    items = ",".join(added_test).replace("_", " ")[:100]
    result += f"Added: {items}. "
if new_pass:
    items = ",".join(new_pass).replace("_", " ")[:100]
    result += f"Passed: {items}. "
if new_fail:
    items = ",".join(new_fail).replace("_", " ")[:100]
    result += f"Failed: {items}. "
print(result)