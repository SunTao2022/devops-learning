"""
Day 2 Bonus: File Extension Counter
Count files by extension in a directory
"""
import os

# Directory to scan (change this to any path)
scan_dir = "."  # current directory

# Get all files and count extensions
ext_count = {}

for item in os.listdir(scan_dir):
    if os.path.isfile(item):
        # Split filename to get extension
        name, ext = os.path.splitext(item)
        ext = ext.lower()  # normalize: .PY, .py → .py
        if ext:
            ext_count[ext] = ext_count.get(ext, 0) + 1
        else:
            ext_count["(no extension)"] = ext_count.get("(no extension)", 0) + 1

# Print results
print(f"Scanning: {os.path.abspath(scan_dir)}")
print(f"Total files: {sum(ext_count.values())}")
print("---")
for ext, count in sorted(ext_count.items(), key=lambda x: -x[1]):
    print(f"  {ext}: {count} file(s)")
