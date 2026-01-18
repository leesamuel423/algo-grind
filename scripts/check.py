#!/usr/bin/env python3
import os
import sys


def check_problem(language, number):
    # Pad problem number with zeros
    padded_number = str(number).zfill(4)

    # Construct directory path
    dir_path = f"{language}/{padded_number}"

    # Check if directory exists
    if os.path.exists(dir_path):
        print(f"✓ Problem {padded_number} exists in {language}")

        # List files in the directory
        files = os.listdir(dir_path)
        if files:
            print(f"  Files: {', '.join(sorted(files))}")
        return True
    else:
        print(f"✗ Problem {padded_number} does NOT exist in {language}")
        print(f"  Expected path: {dir_path}")
        return False


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 scripts/check.py <language> <problem_number>")
        print("Examples:")
        print("  python3 scripts/check.py py 268")
        print("  python3 scripts/check.py cpp 146")
        print("  python3 scripts/check.py java 15")
        print("  python3 scripts/check.py go 3")
        sys.exit(1)

    language = sys.argv[1]

    # Validate language
    valid_languages = ["py", "cpp", "java", "go"]
    if language not in valid_languages:
        print(f"Error: Invalid language '{language}'")
        print(f"Valid languages: {', '.join(valid_languages)}")
        sys.exit(1)

    try:
        number = int(sys.argv[2])
        exists = check_problem(language, number)
        sys.exit(0 if exists else 1)
    except ValueError:
        print("Error: Please provide a valid number")
        sys.exit(1)


if __name__ == "__main__":
    main()
