#!/usr/bin/env python3
# test_grammar.py - Automatic grammar tester for all .tl files in testing/

import sys
from pathlib import Path

# ------------------------------------------------------------------
# Fix Python path so we can import turtparse from ChironCore/
# testing/ is inside ChironCore/, so we add the parent directory
# ------------------------------------------------------------------

script_dir = Path(__file__).parent
chironcore_dir = script_dir.parent
sys.path.insert(0, str(chironcore_dir))

# Import ANTLR4 runtime
from antlr4 import *
import antlr4.error.ErrorListener

# Import generated parser and lexer
from turtparse.tlangLexer import tlangLexer
from turtparse.tlangParser import tlangParser


class ErrorListener(antlr4.error.ErrorListener.ErrorListener):
    """Custom error listener to collect parse errors"""
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Line {line}:{column} - {msg}")


def test_parse(filepath):
    """Test if a file parses correctly"""
    try:
        # Read input
        input_stream = FileStream(str(filepath), encoding='utf-8')

        # Lexer
        lexer = tlangLexer(input_stream)
        token_stream = CommonTokenStream(lexer)

        # Parser
        parser = tlangParser(token_stream)

        # Add error listener to catch errors
        parser.removeErrorListeners()
        error_listener = ErrorListener()
        parser.addErrorListener(error_listener)

        # Parse
        parser.start()

        # Check for errors
        if error_listener.errors:
            return False, error_listener.errors
        else:
            return True, None

    except Exception as e:
        return False, [f"Exception: {str(e)}"]


def find_all_tl_files(testing_dir):
    """Recursively find all .tl files in testing directory"""
    testing_path = Path(testing_dir)

    if not testing_path.exists():
        print(f"Testing directory not found: {testing_dir}")
        return []

    tl_files = list(testing_path.rglob("*.tl"))
    tl_files.sort()

    return tl_files


def get_relative_path(filepath, base_dir):
    """Get relative path from base directory for cleaner output"""
    try:
        return filepath.relative_to(base_dir)
    except ValueError:
        return filepath


def print_header():
    """Print test suite header"""
    print("=" * 80)
    print("  CHIRON TLANG GRAMMAR TESTER")
    print("=" * 80)
    print()


def print_summary(total, passed, failed):
    """Print test summary"""
    print()
    print("=" * 80)
    print("  TEST SUMMARY")
    print("=" * 80)

    if total > 0:
        print(f"  Total tests:  {total}")
        print(f"  Passed:       {passed} ({passed/total*100:.1f}%)")
        print(f"  Failed:       {failed} ({failed/total*100:.1f}%)")
    else:
        print("  No tests found.")

    print("=" * 80)


def main():

    testing_dir = script_dir

    print_header()
    print(f"Scanning directory: {testing_dir}")
    print()

    tl_files = find_all_tl_files(testing_dir)

    if not tl_files:
        print("No .tl files found in testing directory!")
        return

    print(f"Found {len(tl_files)} test file(s)")
    print()
    print("-" * 80)

    passed = 0
    failed = 0
    results = []

    for filepath in tl_files:

        rel_path = get_relative_path(filepath, testing_dir)

        success, errors = test_parse(filepath)

        if success:
            print(f"PASSED: {rel_path}")
            passed += 1
            results.append((rel_path, True, None))
        else:
            print(f"FAILED: {rel_path}")
            for error in errors:
                print(f"         {error}")
            failed += 1
            results.append((rel_path, False, errors))

        print("-" * 80)

    print_summary(len(tl_files), passed, failed)

    if failed > 0:
        print()
        print("=" * 80)
        print("  DETAILED FAILURE REPORT")
        print("=" * 80)

        for rel_path, success, errors in results:
            if not success:
                print(f"\n{rel_path}")
                for error in errors:
                    print(f"   • {error}")

    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()