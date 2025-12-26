#!/usr/bin/env python3
"""
Remove numeric citation markers like [1], [13][14] from markdown files under _posts and _pages.
Creates a .bak backup for each file modified.
"""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
md_files = list(root.glob('_posts/*.md')) + list(root.glob('_pages/*.md')) + list(root.glob('*.md'))
pattern = re.compile(r"\[\d+\]")

for f in md_files:
    text = f.read_text(encoding='utf-8')
    new = pattern.sub('', text)
    # Also remove sequences like ][ that may remain, e.g., after removing, collapse multiple spaces
    new = new.replace('  ', ' ')
    if new != text:
        bak = f.with_suffix(f.suffix + '.bak')
        bak.write_text(text, encoding='utf-8')
        f.write_text(new, encoding='utf-8')
        print(f"Updated {f}")
print('Done')
