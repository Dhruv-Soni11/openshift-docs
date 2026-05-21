#!/usr/bin/env python3
"""
Manual AsciiDoc include resolver (replacement for asciidoctor-reducer)
Recursively resolves include:: directives and applies leveloffset adjustments.
"""

import re
import os
from pathlib import Path

def resolve_includes(content, base_dir, leveloffset=0, visited=None):
    """
    Recursively resolve include:: directives in AsciiDoc content.

    Args:
        content: AsciiDoc content string
        base_dir: Base directory for resolving relative paths
        leveloffset: Current heading level offset
        visited: Set of already-visited files (to prevent circular includes)

    Returns:
        Resolved content string with all includes expanded
    """
    if visited is None:
        visited = set()

    # Pattern to match include:: directives
    # include::path[leveloffset=+N] or include::path[]
    include_pattern = r'^include::([^\[]+)\[(.*?)\]\s*$'

    lines = content.split('\n')
    result = []

    for line in lines:
        match = re.match(include_pattern, line)
        if match:
            include_path = match.group(1)
            attributes = match.group(2)

            # Parse leveloffset from attributes
            offset_match = re.search(r'leveloffset=([+-]\d+)', attributes)
            additional_offset = 0
            if offset_match:
                additional_offset = int(offset_match.group(1))

            # Resolve the include path
            full_path = Path(base_dir) / include_path

            # Prevent circular includes
            if str(full_path) in visited:
                result.append(f"// CIRCULAR INCLUDE DETECTED: {include_path}")
                continue

            # Read the included file
            if full_path.exists():
                visited.add(str(full_path))
                with open(full_path, 'r', encoding='utf-8') as f:
                    included_content = f.read()

                # Recursively resolve includes in the included content
                included_dir = full_path.parent
                resolved_content = resolve_includes(
                    included_content,
                    included_dir,
                    leveloffset + additional_offset,
                    visited.copy()
                )

                # Apply leveloffset to headings in the resolved content
                if leveloffset + additional_offset != 0:
                    resolved_content = adjust_headings(resolved_content, leveloffset + additional_offset)

                result.append(resolved_content)
            else:
                result.append(f"// INCLUDE NOT FOUND: {include_path}")
        else:
            result.append(line)

    return '\n'.join(result)

def adjust_headings(content, offset):
    """
    Adjust AsciiDoc heading levels by adding/removing = characters.

    Args:
        content: AsciiDoc content
        offset: Number of levels to adjust (+/-)

    Returns:
        Content with adjusted headings
    """
    if offset == 0:
        return content

    lines = content.split('\n')
    result = []

    for line in lines:
        # Match AsciiDoc headings (= Title, == Title, etc.)
        heading_match = re.match(r'^(=+)\s+(.*)$', line)
        if heading_match:
            current_equals = heading_match.group(1)
            title = heading_match.group(2)

            # Calculate new level
            new_level = len(current_equals) + offset
            if new_level < 1:
                new_level = 1  # Minimum heading level

            new_equals = '=' * new_level
            result.append(f"{new_equals} {title}")
        else:
            result.append(line)

    return '\n'.join(result)

def reduce_assembly(assembly_path, output_path):
    """
    Reduce an AsciiDoc assembly by resolving all includes.

    Args:
        assembly_path: Path to the assembly file
        output_path: Path for the reduced output file
    """
    assembly_path = Path(assembly_path)
    output_path = Path(output_path)

    # Read the assembly file
    with open(assembly_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Resolve includes relative to the assembly directory
    base_dir = assembly_path.parent
    reduced_content = resolve_includes(content, base_dir)

    # Write the reduced content
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(reduced_content)

    print(f"Reduced assembly written to: {output_path}")
    print(f"Total lines: {len(reduced_content.split(chr(10)))}")

if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print("Usage: reduce_assembly.py <assembly_path> <output_path>")
        sys.exit(1)

    assembly_path = sys.argv[1]
    output_path = sys.argv[2]

    reduce_assembly(assembly_path, output_path)
