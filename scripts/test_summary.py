#!/usr/bin/env python3
"""Parse bazel test output and print a colored summary grid."""

import re
import sys
from collections import defaultdict

GREEN_BG = "\033[42;30m"
RED_BG = "\033[41;30m"
BOLD = "\033[1m"
RESET = "\033[0m"
LINE = "──────────────────────────────────────────────────────────────"
ITEMS_PER_ROW = 10
LABEL_WIDTH = 7


def parse_results(filepath):
    tests = defaultdict(list)
    pattern = re.compile(r"^//(\w+)/(\d+):test\s+(?:\(cached\)\s+)?(PASSED|FAILED)")
    with open(filepath) as f:
        for line in f:
            m = pattern.search(line.strip())
            if m:
                lang, num, result = m.groups()
                tests[lang].append((num, result == "PASSED"))
    for lang in tests:
        tests[lang].sort()
    return tests


def print_summary(tests):
    passed = sum(1 for t in tests.values() for _, p in t if p)
    failed = sum(1 for t in tests.values() for _, p in t if not p)

    print(f"\n  {LINE}")
    print(f"  {BOLD}Test Summary{RESET}")
    print(f"  {LINE}")

    for lang in sorted(tests):
        items = tests[lang]
        for i, (num, ok) in enumerate(items):
            if i % ITEMS_PER_ROW == 0:
                if i == 0:
                    print(f"  {BOLD}{lang:<{LABEL_WIDTH}}{RESET}", end="")
                else:
                    print(f"\n  {'':<{LABEL_WIDTH}}", end="")
            bg = GREEN_BG if ok else RED_BG
            print(f" {bg} {num} {RESET}", end="")
        print()

    print(f"  {LINE}")

    if failed:
        print(f"  {RED_BG} {passed} passed, {failed} failed {RESET}")
        print()
        for lang in sorted(tests):
            for num, ok in tests[lang]:
                if not ok:
                    print(f"  {RED_BG} FAIL {RESET} //{lang}/{num}:test")
    else:
        print(f"  {GREEN_BG} {passed} passed {RESET}")
    print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <bazel-output-file>", file=sys.stderr)
        sys.exit(1)
    tests = parse_results(sys.argv[1])
    if tests:
        print_summary(tests)
