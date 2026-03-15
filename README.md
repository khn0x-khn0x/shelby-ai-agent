# Shelby AI Agent Pipeline

This project implements an automated, event-driven data integrity pipeline for Shelby.

## Architecture
1. **File Monitoring:** Uses `watchdog` to detect new datasets in the `data/` directory.
2. **Integrity:** Automatically computes **SHA-256** hashes for every file.
3. **Audit Ledger:** Maintains a `manifest.json` for verifiable history.

## Getting Started
1. Install dependencies: `pip install watchdog`
2. Run the watcher: `python scripts/watcher.py`
