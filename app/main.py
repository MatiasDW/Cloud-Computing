from fastapi import FastAPI
from app.authentication.router import router as auth_router
from app.files.router import router as files_router

app = FastAPI()

@app.get("/healthcheck")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}

# Include routers for authentication and files
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(files_router, prefix="/files", tags=["Files"])
