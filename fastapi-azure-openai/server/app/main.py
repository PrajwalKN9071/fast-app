from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import generate_text
from app.api.v1.endpoints import facebook

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],  # Adjust this to your client URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(generate_text.router, prefix="/api/v1")

app.include_router(facebook.router, prefix="/api/v1/facebook")

@app.get("/test")
async def test():
    return {"message": "Test endpoint working"}









