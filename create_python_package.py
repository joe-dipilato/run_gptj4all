#!/usr/bin/env python3
"""
This file will create a new fully templated python package from scratch.
It will include all standard python files for a package including:
__init__.py, __main__.py, __test__.py, and setup.py
It will also include subpackages with template files including:
test, docs, examples, common, util, engine, etc..
It will also automatically populate the contents of the files such that
it is ready to use.
"""

import sys
from pathlib import Path
import argparse
# import structlog
from typing import *
from dataclasses import dataclass
from typing import Union

@dataclass
class CreatePackageArgs:
    package: str = "default"
    version: str = "0.0.1"
    directory: Path =  Path.cwd()

# log = structlog.get_logger()

class CreatePackage:
    """
    This class will create a new python package.
    """
    def __init__(self, package_args: CreatePackageArgs = CreatePackageArgs()) -> None:
        """
        Create a new python package.
        :param args: The arguments to create the package with.
        """
        self.args = self.parse_args_from_package_args(package_args)

    def parse_args_from_command_line(self) -> argparse.Namespace:
        """
        Parse the command line arguments.
        This will only be used when running from command line
        :return:
        """
        options = argparse.ArgumentParser(description="Create a new python package.")
        options.add_argument("-p", "--package", help="The name of the package to create.",
                             default="default")
        options.add_argument("-v", "--version", help="The version of the package to create.",
                             default="0.0.1")
        options.add_argument("-d", "--directory", help="The directory to create the package in.",
                             default=Path.cwd())
        return options.parse_args()

    def convert_package_args_to_dict(self, package_args: CreatePackageArgs) -> Dict[str, Any]:
        """
        Convert the package args to a dictionary.
        This will only be used when converting a package args to a dictionary.
        :param package_args:
        :return:
        """
        return vars(package_args)

    def parse_args_from_package_args(self, package_args: CreatePackageArgs) -> argparse.Namespace:
        """
        Parse the args from the package args.
        This will only be used when setting arguments from a package args.
        :param package_args:
        :return:
        """
        return self.parse_args_from_dict(self.convert_package_args_to_dict(package_args))
    
    def parse_args_from_dict(self, args: Dict[str, Any]) -> argparse.Namespace:
        """
        Set the command line arguments.
        This will only be used when setting arguments from a dictionary.
        :param args:
        :return:
        """
        return argparse.Namespace(**args)

    def run(self):
        """
        Run the application.
        :return:
        """
        self.parse_args_from_command_line()
        self.create_package()
        return 0

    def create_package(self):
        pass

    def create_subpackage(self):
        pass

    def create_init(self):
        pass

    def create_main(self):
        pass

    def create_test(self):
        pass

    def create_subpackage_from_template(self):
        pass

# This section is for the unit tests that will be run with pytest
class TestCreatePackage():
    """
    This class will test the CreatePackage class.
    """
    def test_create_package_from_command_line(self):
        """
        Test the parse_args_from_command_line method.
        :return:
        """
        sys.args = ["create_python_package.py", "-p", "test", "-v", "0.0.1", "-d", "test_package"]
        app = CreatePackage()
        app.parse_args_from_command_line()
        app.create_package()

    def test_create_package_from_dict(self):
        """
        Test the parse_args_from_dict method.
        :return:
        """
        app = CreatePackage()
        app.parse_args_from_dict({"package": "test", "version": "0.0.1", "directory": "test_package"})
        app.create_package()

    def test_create_package_from_package_args(self):
        """
        Test the test_create_package_from_package_args method.
        :return:
        """
        app = CreatePackage(CreatePackageArgs(package="test", version="0.0.1", directory="test_package"))
        app.create_package()

       

if __name__ == "__main__":
    app = CreatePackage()
    sys.exit(app.run())