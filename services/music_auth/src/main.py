from api.routes import oauth
from fastapi import FastAPI

app = FastAPI(title="Music Auth Service")

app.include_router(oauth.router)
