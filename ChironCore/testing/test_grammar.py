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
    """Custom error listener to collect parse and lexer errors quietly"""
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Line {line}:{column} - {msg}")


def test_parse(filepath):
    """Test if a file parses correctly"""
    try:
        # Read input
        input_stream = FileStream(str(filepath), encoding='utf-8')

        # Create custom error listener
        error_listener = ErrorListener()

        # Lexer
        lexer = tlangLexer(input_stream)
        lexer.removeErrorListeners() # Remove default console output
        lexer.addErrorListener(error_listener) # Add custom listener
        
        token_stream = CommonTokenStream(lexer)

        # Parser
        parser = tlangParser(token_stream)
        parser.removeErrorListeners() # Remove default console output
        parser.addErrorListener(error_listener) # Add custom listener

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

    test_passed_count = 0
    test_failed_count = 0
    results = []

    for filepath in tl_files:

        rel_path = get_relative_path(filepath, testing_dir)
        filename = filepath.name.lower()
        
        # Determine if this file is *expected* to fail parsing
        expected_to_fail = "incorrect" in filename

        parse_success, errors = test_parse(filepath)

        # Evaluate the test outcome
        if expected_to_fail:
            if not parse_success:
                test_status = "PASSED"
                reason = "EXPECTED FAILURE (Caught syntax errors correctly)"
                is_test_success = True
            else:
                test_status = "FAILED"
                reason = "UNEXPECTED SUCCESS (Should have failed syntax check but didn't)"
                is_test_success = False
        else:
            if parse_success:
                test_status = "PASSED"
                reason = "EXPECTED SUCCESS (Parsed correctly)"
                is_test_success = True
            else:
                test_status = "FAILED"
                reason = "UNEXPECTED FAILURE (Failed to parse correctly)"
                is_test_success = False

        # Print per-file result
        print(f"[{test_status}] {rel_path}")
        print(f"         {reason}")
        
        if is_test_success:
            test_passed_count += 1
        else:
            test_failed_count += 1
            
        results.append((rel_path, is_test_success, reason, errors, expected_to_fail))
        print("-" * 80)

    print_summary(len(tl_files), test_passed_count, test_failed_count)

    # Only print detailed failure report for ACTUAL test framework failures
    if test_failed_count > 0:
        print()
        print("=" * 80)
        print("  DETAILED FAILURE REPORT (Unexpected Outcomes)")
        print("=" * 80)

        for rel_path, is_test_success, reason, errors, expected_to_fail in results:
            if not is_test_success:
                print(f"\n{rel_path}")
                print(f"   Issue: {reason}")
                if errors:
                    print("   Errors caught during parsing:")
                    for error in errors:
                        print(f"     • {error}")

    sys.exit(0 if test_failed_count == 0 else 1)


if __name__ == "__main__":
    main()