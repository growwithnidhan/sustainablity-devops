# green_trigger.py
import subprocess
import sys

# Get list of changed files compared to main branch
changed_files = subprocess.getoutput("git diff --name-only origin/main").splitlines()

# Map files to modules
module_tests = {
    "app/addition.py": "tests/test_addition.py",
    "app/subtraction.py": "tests/test_subtraction.py",
}

# Determine which tests to run
tests_to_run = [module_tests[f] for f in changed_files if f in module_tests]

if not tests_to_run:
    print("No relevant module changes. Skipping tests.")
    sys.exit(0)

print(f"Running tests for changed modules: {tests_to_run}")
# Run the selected tests
for test_file in tests_to_run:
    subprocess.run(["pytest", test_file], check=True)
