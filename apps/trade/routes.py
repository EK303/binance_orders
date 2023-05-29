from typing import List, Annotated

from fastapi import APIRouter, status, HTTPException, Depends

from apps.config import settings
from apps.auth.routes import get_current_user
from apps.auth.models import User

from .schemas import AccountBalance, OrderSchema
from .service import PortfolioService
from .utils import check_order

portfolio_service = PortfolioService.get_instance()

trade_router = APIRouter()

client = settings.TESTNET_CLIENT


@trade_router.get("/account/balance",
                  response_model=List[AccountBalance],
                  status_code=status.HTTP_200_OK,
                  tags=["trade"], )
async def my_portfolio():
    portfolio = portfolio_service.get_portfolio()

    return portfolio


@trade_router.post("/account/order",
                   status_code=status.HTTP_201_CREATED,
                   tags=["trade"])
async def place_order(order: OrderSchema):
    order_place = check_order(**order.dict())

    if not order_place.status:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=order_place.message)

    return {"message": "Order placed successfully"}
