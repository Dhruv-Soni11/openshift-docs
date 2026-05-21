#!/usr/bin/env python3
"""
Convert JTBD JSONL to CSV format.
"""

import json
import csv
from pathlib import Path

def jsonl_to_csv(jsonl_path, csv_path):
    """Convert JSONL file to CSV."""
    jsonl_path = Path(jsonl_path)
    csv_path = Path(csv_path)

    # Read all records
    records = []
    with open(jsonl_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))

    if not records:
        print("No records found in JSONL file")
        return

    # Determine all unique keys across all records
    all_keys = set()
    for record in records:
        all_keys.update(record.keys())

    # Sort keys for consistent column order
    fieldnames = sorted(all_keys)

    # Write CSV
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for record in records:
            # Convert arrays to semicolon-separated strings
            row = {}
            for key in fieldnames:
                value = record.get(key)
                if isinstance(value, list):
                    row[key] = '; '.join(str(v) for v in value)
                elif value is None:
                    row[key] = ''
                else:
                    row[key] = str(value)
            writer.writerow(row)

    print(f"CSV written to: {csv_path}")
    print(f"Total records: {len(records)}")

if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print("Usage: convert_to_csv.py <jsonl_path> <csv_path>")
        sys.exit(1)

    jsonl_path = sys.argv[1]
    csv_path = sys.argv[2]

    jsonl_to_csv(jsonl_path, csv_path)
