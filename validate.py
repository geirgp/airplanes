#!/usr/bin/env python3
"""
Aircraft XML Validation Script
Validates all .aircraft files against aircraft.xsd schema
"""

import sys
import os
import subprocess
import glob
from pathlib import Path

SCHEMA_FILE = "aircraft.xsd"

def check_xmllint():
    """Check if xmllint is available."""
    try:
        subprocess.run(["xmllint", "--version"], 
                      capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def validate_file(schema_file, xml_file):
    """Validate a single XML file against the schema."""
    try:
        result = subprocess.run(
            ["xmllint", "--noout", "--schema", schema_file, xml_file],
            capture_output=True,
            text=True
        )
        return result.returncode == 0, result.stderr
    except FileNotFoundError:
        return False, "xmllint not found"

def main():
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # Check if xmllint is available
    if not check_xmllint():
        print("Error: xmllint is not installed", file=sys.stderr)
        print("Install it with: brew install libxml2", file=sys.stderr)
        sys.exit(1)
    
    # Check if schema file exists
    if not Path(SCHEMA_FILE).exists():
        print(f"Error: Schema file '{SCHEMA_FILE}' not found", file=sys.stderr)
        sys.exit(1)
    
    # Find all .aircraft files
    if len(sys.argv) > 1:
        aircraft_files = sys.argv[1:]
    else:
        aircraft_files = sorted(glob.glob("*.aircraft"))
    
    if not aircraft_files:
        print("Warning: No .aircraft files found", file=sys.stderr)
        sys.exit(0)
    
    print(f"Validating aircraft files against {SCHEMA_FILE}...")
    print()
    
    valid_count = 0
    invalid_count = 0
    invalid_files = []
    
    # Validate each file
    for file in aircraft_files:
        if not Path(file).exists():
            continue
        
        print(f"Checking {file}... ", end="", flush=True)
        is_valid, error_msg = validate_file(SCHEMA_FILE, file)
        
        if is_valid:
            print("✓ Valid")
            valid_count += 1
        else:
            print("✗ Invalid")
            invalid_count += 1
            invalid_files.append((file, error_msg))
    
    print()
    print("=" * 42)
    print("Validation Summary:")
    print(f"  Valid:   {valid_count}")
    print(f"  Invalid: {invalid_count}")
    print(f"  Total:   {valid_count + invalid_count}")
    print("=" * 42)
    
    # Exit with error code if any files failed validation
    if invalid_count > 0:
        print()
        print("The following files failed validation:")
        for file, error_msg in invalid_files:
            print(f"  - {file}")
            if error_msg:
                print(f"    {error_msg}")
        sys.exit(1)
    else:
        print()
        print("All files validated successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()

