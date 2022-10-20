import argparse
import pytest


parser = argparse.ArgumentParser(description="Tests runner")
parser.add_argument("-a", "--all", action="store_true", help="runs all tests in this framework")
parser.add_argument("-t2", "--test2", action="store_true", help="run test2")
parser.add_argument("-t1", "--test1", action="store_true", help="run test1")



args = parser.parse_args()
if args.all:
    pytest.main(args=["-v", "tests.py"])
elif args.test2:
    pytest.main(args=["-v", "tests.py::TestSignUpPage::test_s"])
elif args.test1:
    pytest.main(args=["-v", "tests.py::TestSignUpPage::test_signup"])
print(args)
