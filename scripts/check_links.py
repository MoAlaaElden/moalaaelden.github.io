#!/usr/bin/env python3
"""Simple internal link checker for generated Jekyll site in _site.
Skips external (http/https) and mailto/tel links. Checks file existence for internal paths.
"""
import re
from pathlib import Path

root = Path('_site')
html_files = list(root.rglob('*.html'))
link_re = re.compile(r'(?:href|src)="([^"]+)"')

broken = []

for f in html_files:
    text = f.read_text(encoding='utf-8', errors='ignore')
    for match in link_re.findall(text):
        link = match.split('#')[0].split('?')[0]
        if not link or link.startswith('http') or link.startswith('mailto:') or link.startswith('tel:'):
            continue
        # ignore theme docs and known theme asset patterns (e.g., Minimal Mistakes docs/images)
        exclude_prefixes = ('/docs/', '/assets/images/mm-')
        if any(link.startswith(p) for p in exclude_prefixes):
            continue
        # handle fragments only
        if link.startswith('#'):
            continue
        # absolute path
        if link.startswith('/'):
            target = root / link.lstrip('/')
        else:
            target = (f.parent / link).resolve()
            # convert to path relative to cwd
            try:
                target = Path(target).relative_to(Path.cwd())
            except Exception:
                pass
            # if link is relative path, join with root if it starts with _site
        # try several candidates
        candidates = []
        candidates.append(Path(target))
        if Path(target).is_dir() or str(target).endswith('/'):
            candidates.append(Path(target) / 'index.html')
        if Path(target).suffix == '':
            candidates.append(Path(str(target) + '.html'))
            candidates.append(Path(str(target) + '/index.html'))
        # normalize paths
        found = False
        for c in candidates:
            # resolve if relative to cwd
            c = Path(c)
            # if c is absolute to file system, check exists
            if c.exists():
                found = True
                break
            # try relative to root
            rel = root / c
            if rel.exists():
                found = True
                break
        if not found:
            broken.append((str(f), match))

if broken:
    print('Broken links found:')
    for f, l in broken:
        print(f'- {f}: {l}')
    raise SystemExit(2)
else:
    print('No broken internal links found')
