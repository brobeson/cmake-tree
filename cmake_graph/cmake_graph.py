"""Generate a dependency graph for a CMake project."""

import argparse
import glob
import os.path
import sys


def main():
    """Main entry point for the application."""
    arguments = parse_command_line()
    cmake_files = get_cmake_files(arguments.project)
    if not cmake_files:
        print("No CMake files were found in", arguments.project)
        return
    print(cmake_files)


def parse_command_line():
    """Parse the command line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate a dependency graph of a CMake project."
    )
    parser.add_argument(
        "project",
        help="The path to the project to analyze.",
        default=os.path.abspath("."),
    )
    arguments = parser.parse_args()
    arguments.project = os.path.abspath(os.path.expanduser(arguments.project))
    return arguments


def get_cmake_files(project):
    os.chdir(project)
    files = glob.glob("**/CMakeLists.txt", recursive=True)
    files.extend(glob.glob("**/*.cmake", recursive=True))
    return files


if __name__ == "__main__":
    main()
    sys.exit(0)
