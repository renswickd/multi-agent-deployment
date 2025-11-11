import sys
from pathlib import Path
import os

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

import uvicorn
import threading
import subprocess
# import streamlit as st
from fastapi import FastAPI
from app.backend.api import router
from app.config.params import load_yaml_config

config = load_yaml_config()
print(config["urls_and_ports"])

app = FastAPI(title="AI Agent App Deployment Demo", version="0.1")
app.include_router(router, prefix="/api")

def run_backend():
    uvicorn.run("main:app", host=config["urls_and_ports"]["backend_host"], port=config["urls_and_ports"]["backend_port"], reload=False)

def run_frontend():
    env = os.environ.copy()
    env["PYTHONPATH"] = str(project_root)
    subprocess.run(
        ["streamlit", "run", "app/frontend/ui.py"],
        env=env
    )

def main():
    # Create threads for frontend and backend
    backend_thread = threading.Thread(target=run_backend)
    frontend_thread = threading.Thread(target=run_frontend)

    try:
        backend_thread.start()
        print("backend started")

        frontend_thread.start()
        print("frontend started")
        
        backend_thread.join()
        frontend_thread.join()

    except KeyboardInterrupt:
        print("Shutting down servers...")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()