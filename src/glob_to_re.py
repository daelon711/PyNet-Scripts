import glob
import re


def glob_to_regex():
    # ask the user for a glob pattern
    pattern = input("your glob pattern (e.g: '**/*.txt'): ")
    # converts that glob pattern into a regex string
    regex_pattern = glob.translate(
        pattern, recursive=True, include_hidden=True)
    print(f"Translated regex pattern: {regex_pattern}")

    # regex pattern string into a regex object
    reobj = re.compile(regex_pattern)

    #  check if a specific filename or path matches the original glob pattern
    test_string = input(
        "Enter string (file path) to match with the regex: ")
    if reobj.match(test_string):
        print(
            f"'{test_string}' matches the glob pattern '{pattern}'.")
    else:
        print(
            f"'{test_string}' does NOT match the glob pattern '{pattern}'.")

    return regex_pattern


if __name__ == '__main__':
    glob_to_regex()
