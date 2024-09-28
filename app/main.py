"""main run file."""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.ping import router as ping_router

app = FastAPI()

# Allow CORS for all origins for now (adjust for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files like CSS and JS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Mount the ping API router
app.include_router(ping_router)

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def read_root(request: Request):
    """API home for dashboard."""
    return templates.TemplateResponse("index.html", {"request": request})
