from fastapi import FastAPI
from app.backend.api import router # Assuming your api.py is structured like this

app = FastAPI(title="AI Agent API")

app.include_router(router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    # This runs the application when you execute the script directly
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 