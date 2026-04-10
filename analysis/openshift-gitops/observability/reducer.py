#!/usr/bin/env python3
"""
Simple AsciiDoc include resolver for OpenShift docs.
Resolves include:: directives by reading and inserting the referenced files.
"""

import re
import sys
from pathlib import Path


def resolve_includes(content, base_dir, max_depth=5, current_depth=0):
    """Recursively resolve include directives in AsciiDoc content."""
    if current_depth >= max_depth:
        return content

    # Pattern: include::path/to/file.adoc[leveloffset=+1]
    include_pattern = re.compile(r'^include::([^\[]+)\[([^\]]*)\]\s*$', re.MULTILINE)

    def replace_include(match):
        include_path = match.group(1)
        attrs = match.group(2)

        # Resolve the file path
        full_path = base_dir / include_path

        if not full_path.exists():
            return f"// ERROR: Could not find {include_path}\n"

        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                included_content = f.read()

            # Recursively resolve includes in the included content
            included_content = resolve_includes(
                included_content,
                base_dir,
                max_depth,
                current_depth + 1
            )

            # Add a comment showing where this content came from
            return f"// Included from: {include_path}\n{included_content}\n"
        except Exception as e:
            return f"// ERROR including {include_path}: {str(e)}\n"

    return include_pattern.sub(replace_include, content)


def main():
    if len(sys.argv) != 3:
        print("Usage: reducer.py <input.adoc> <output.adoc>")
        sys.exit(1)

    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2])

    if not input_file.exists():
        print(f"Error: Input file {input_file} does not exist")
        sys.exit(1)

    # Base directory is the directory containing the input file
    base_dir = input_file.parent.parent

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    reduced_content = resolve_includes(content, base_dir)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(reduced_content)

    print(f"Reduced {input_file} -> {output_file}")


if __name__ == '__main__':
    main()
