from fastapi import FastAPI
from api.v1.routes import router as api_router

app = FastAPI(title="Cookit API")

app.include_router(api_router, prefix="/api/v1")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
