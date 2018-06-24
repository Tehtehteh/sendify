import sys

from os import path

from unittest import TestLoader, TextTestRunner


def main():
    suite = TestLoader().discover(start_dir=path.join(path.dirname(__file__), 'test_cases'))
    runner = TextTestRunner(verbosity=2)
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)  # For non 0 exit code :0


if __name__ == '__main__':
    main()
