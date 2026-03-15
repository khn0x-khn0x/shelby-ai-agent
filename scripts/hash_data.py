import hashlib
import json
import sys
import os

def hash_file(file_path):
    if not os.path.exists(file_path):
        return None
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/hash_data.py <file_path>")
    else:
        path = sys.argv[1]
        result = hash_file(path)
        if result:
            print(f"Hash file {path}: {result}")
        else:
            print(f"Error: File {path} was not found!")
