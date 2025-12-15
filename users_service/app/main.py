# app/main.py - исправленная версия
import os
print("Starting users_service...")
print(f"Current dir: {os.getcwd()}")
print(f"Files: {os.listdir('.')}")

from fastapi import FastAPI
from routers import router

app = FastAPI(title="Users Service")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Users Service Working"}

@app.get("/health")
def health():
    return {"status": "ok"}

print("=== Service ready ===")