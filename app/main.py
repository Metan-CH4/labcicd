import os
from fastapi import FastAPI
app = FastAPI()

@app.get("/health")
def health(): return {"status": "ok"}

@app.get("/")
def root(): return {"service": "demo", "version": os.getenv("APP_VERSION", "dev")}