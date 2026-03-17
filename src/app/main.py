from fastapi import FastAPI
app = FastAPI(
    title="FastAPI Notes API",
    description="A simple API to manage notes, built with FastAPI.",
    version="0.1.0")

@app.get("/")
async def root():
  return {"message": "Welcome to the FastAPI Notes API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}