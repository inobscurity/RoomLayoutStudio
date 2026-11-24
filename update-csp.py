#!/usr/bin/env python3
"""Set the Content-Security-Policy in index.html.

The policy lets the page run only its own inline script (identified by its SHA-256 hash) and the 3D
library from cdn.jsdelivr.net, load fonts from Google Fonts, and show images only from data: and blob:
URLs. It allows no network connections and no plugins. Any injected script or inline event handler is
refused by the browser.

Run this after every change to the script in index.html:  python3 update-csp.py
(If you forget, the app shows a blank page, because the browser blocks the changed script.)
"""
import base64, hashlib, pathlib, re

path = pathlib.Path(__file__).with_name("index.html")
html = path.read_text(encoding="utf-8")
m = re.search(r"<script>(.*?)</script>", html, re.S)
if not m:
    raise SystemExit("No inline <script> found")
digest = base64.b64encode(hashlib.sha256(m.group(1).encode("utf-8")).digest()).decode()
policy = "; ".join([
    "default-src 'none'",
    f"script-src 'sha256-{digest}' https://cdn.jsdelivr.net",
    "style-src 'unsafe-inline' https://fonts.googleapis.com",
    "font-src https://fonts.gstatic.com",
    "img-src data: blob:",
    "connect-src 'none'",
    "worker-src 'none'",
    "object-src 'none'",
    "base-uri 'none'",
    "form-action 'none'",
])
new, n = re.subn(r'(<meta http-equiv="Content-Security-Policy" content=")[^"]*(">)', lambda mm: mm.group(1) + policy + mm.group(2), html)
if n != 1:
    raise SystemExit("Content-Security-Policy meta tag not found")
path.write_text(new, encoding="utf-8")
print("CSP updated: script sha256-" + digest)
