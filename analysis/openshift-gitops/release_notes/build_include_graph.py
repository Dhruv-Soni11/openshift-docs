#!/usr/bin/env python3
"""
Build an include graph showing the relationship between assemblies and modules.
Maps module paths to their types (CONCEPT, PROCEDURE, REFERENCE, SNIPPET).
"""

import re
import json
from pathlib import Path

def detect_module_type(module_path):
    """
    Detect module type from filename prefix.

    Args:
        module_path: Path to the module file

    Returns:
        Module type string (CONCEPT, PROCEDURE, REFERENCE, SNIPPET, UNKNOWN)
    """
    filename = Path(module_path).name

    if filename.startswith('con-'):
        return 'CONCEPT'
    elif filename.startswith('proc-'):
        return 'PROCEDURE'
    elif filename.startswith('ref-'):
        return 'REFERENCE'
    elif filename.startswith('snip-'):
        return 'SNIPPET'
    else:
        # Check common patterns
        if 'release-notes' in filename or 'compatibility' in filename:
            return 'REFERENCE'
        return 'UNKNOWN'

def parse_includes(assembly_path, base_dir):
    """
    Parse include:: directives from an assembly file.

    Args:
        assembly_path: Path to the assembly file
        base_dir: Base directory for resolving relative paths

    Returns:
        List of dicts with include information
    """
    include_pattern = r'^include::([^\[]+)\[(.*?)\]\s*$'
    includes = []

    with open(assembly_path, 'r', encoding='utf-8') as f:
        content = f.read()

    for line_num, line in enumerate(content.split('\n'), 1):
        match = re.match(include_pattern, line)
        if match:
            include_path = match.group(1)
            attributes = match.group(2)

            # Parse leveloffset
            offset_match = re.search(r'leveloffset=([+-]\d+)', attributes)
            leveloffset = offset_match.group(1) if offset_match else None

            # Resolve full path
            full_path = Path(base_dir) / include_path

            # Skip attribute includes
            if '_attributes' in include_path:
                continue

            # Detect module type
            module_type = detect_module_type(include_path)

            includes.append({
                'line_number': line_num,
                'include_path': include_path,
                'resolved_path': str(full_path),
                'leveloffset': leveloffset,
                'module_type': module_type,
                'exists': full_path.exists()
            })

    return includes

def build_include_graph(assembly_path, output_path):
    """
    Build an include graph JSON file.

    Args:
        assembly_path: Path to the assembly file
        output_path: Path for the output JSON file
    """
    assembly_path = Path(assembly_path)
    output_path = Path(output_path)

    base_dir = assembly_path.parent

    # Parse includes
    includes = parse_includes(assembly_path, base_dir)

    # Build graph structure
    graph = {
        'assembly': str(assembly_path),
        'base_directory': str(base_dir),
        'total_includes': len(includes),
        'includes': includes,
        'module_type_counts': {}
    }

    # Count module types
    for inc in includes:
        module_type = inc['module_type']
        graph['module_type_counts'][module_type] = graph['module_type_counts'].get(module_type, 0) + 1

    # Write to JSON
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(graph, f, indent=2)

    print(f"Include graph written to: {output_path}")
    print(f"Total includes: {len(includes)}")
    print(f"Module type counts: {graph['module_type_counts']}")

if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print("Usage: build_include_graph.py <assembly_path> <output_path>")
        sys.exit(1)

    assembly_path = sys.argv[1]
    output_path = sys.argv[2]

    build_include_graph(assembly_path, output_path)
