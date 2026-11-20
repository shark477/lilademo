"""Embed the three minimaps (resized to 1024x1024 JPEG) into index.template.html -> index.html.
Usage: python3 build.py <AmbroseValley_Minimap.png> <GrandRift_Minimap.png> <Lockdown_Minimap.jpg>
Requires: pip install pillow"""
import base64, io, sys
from PIL import Image
if len(sys.argv) != 4: sys.exit(__doc__)
html = open("index.template.html", encoding="utf-8").read()
for key, path in zip(["AV", "GR", "LD"], sys.argv[1:]):
    im = Image.open(path).convert("RGB").resize((1024, 1024), Image.LANCZOS)
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=82)
    html = html.replace(f"__{key}__", "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode())
open("index.html", "w", encoding="utf-8").write(html)
print("wrote index.html", len(html) // 1024, "KB")
