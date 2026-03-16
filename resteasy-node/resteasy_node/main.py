from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from resteasy_node import info
from resteasy_node.routes import misc


# The main FastAPI application instance
app = FastAPI(
    title=info.NAME,
    version=info.VERSION,
    root_path="/api",
)

# Include all route modules
app.include_router(misc.router)

# Add CORS middleware to allow cross-origin requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods="*",
    allow_headers="*",
)
