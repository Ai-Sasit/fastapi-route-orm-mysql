from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.user_route import user
import uvicorn
import colorama

colorama.init(autoreset=True)

app = FastAPI(docs_url="/api/docs", redoc_url="/api/redoc")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user, prefix="/api", tags=["User"])

if __name__ == "__main__":
    uvicorn.run("server:app", host="localhost", reload=True, port=9100)