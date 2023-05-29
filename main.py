from fastapi import FastAPI

from apps.auth.routes import auth_router
from apps.trade.routes import trade_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(trade_router)
