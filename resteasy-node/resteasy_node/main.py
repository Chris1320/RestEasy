from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from resteasy_node import info
from resteasy_node.routes import misc


app = FastAPI(
    title=info.NAME,
    version=info.VERSION,
    root_path="/api",
)

app.include_router(misc.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods="*",
    allow_headers="*",
)
