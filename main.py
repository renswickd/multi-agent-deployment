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
    uvicorn.run("main:app", host=config["urls_and_ports"], port=config["backend_port"], reload=False)

def run_frontend():
    subprocess.run(["streamlit", "run", "app/frontend/ui.py"])

def main():
    # Create threads for frontend and backend
    backend_thread = threading.Thread(target=run_backend)
    frontend_thread = threading.Thread(target=run_frontend)

    try:
        backend_thread.start()
        frontend_thread.start()

        backend_thread.join()
        frontend_thread.join()

    except KeyboardInterrupt:
        print("Shutting down servers...")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()