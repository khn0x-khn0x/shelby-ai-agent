import os
import sys
from dotenv import load_dotenv

# Loads variables from the .env file in the root folder
load_dotenv(dotenv_path=".env")

REQUIRED_VARS = [
    "SHELBY_API_KEY",
    "APTOS_RPC_URL",
    "SHELBY_CONTEXT_ID"
]

def check_environment():
    print("🔍 I am checking the environment settings...")
    missing = []
    
    for var in REQUIRED_VARS:
        if os.getenv(var):
            print(f"✅ {var} is set.")
        else:
            missing.append(var)
    
    if missing:
        print(f"\n❌ These variables are missing: {', '.join(missing)}")
        print("💡 Create a file '.env' in the root folder and set them.")
        sys.exit(1)
    else:
        print("\n🚀 The environment is ready! You can start integration.")

if __name__ == "__main__":
    check_environment()
