import time
import json
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from hash_data import hash_file

# The name of the file where we will save the history
MANIFEST_FILE = "manifest.json"

class DataHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"\n📂 New file detected: {event.src_path}")
            
            # We calculate the hash using our function
            file_hash = hash_file(event.src_path)
            print(f"🔑 Calculated SHA-256: {file_hash}")
            
            # We are updating the manifest
            self.update_manifest(event.src_path, file_hash)

    def update_manifest(self, file_path, file_hash):
        manifest = {}
        
        # If the manifest already exists, we load it
        if os.path.exists(MANIFEST_FILE):
            with open(MANIFEST_FILE, "r") as f:
                try:
                    manifest = json.load(f)
                except json.JSONDecodeError:
                    manifest = {}
        
        # We will add a new record
        file_name = os.path.basename(file_path)
        manifest[file_name] = {
            "hash": file_hash,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        }
        
        # We save the updated manifest back
        with open(MANIFEST_FILE, "w") as f:
            json.dump(manifest, f, indent=4)
        print(f"✅ Manifest updated: {MANIFEST_FILE}")

# Tracking settings
observer = Observer()
observer.schedule(DataHandler(), path='data/', recursive=False)
observer.start()

print("🚀 I am following the folder data/... (press Ctrl+C to exit)")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
