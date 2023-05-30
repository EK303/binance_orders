import time

from typing import List

from fastapi import APIRouter, status, HTTPException

from apps.config import settings

from .schemas import AccountBalance, OrderSchema
from .service import PortfolioService
from .utils import check_order
from .creating_orders import generate_orders, generate_random_prices

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
    order_dict = order.dict()
    order_place = check_order(**order_dict)

    if not order_place.status:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=order_place.message)

    generated_prices = generate_random_prices(order_dict["number"], order_dict["priceMin"], order_dict["priceMax"])

    if not generated_prices.status:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=generated_prices.message)

    generated_coefficients = generate_orders(generated_prices.data, order_dict["volume"], order_dict["amountDif"])

    if not generated_coefficients.status:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=generated_coefficients.message)

    coefficients, market_prices = generated_coefficients.data

    len_coefficients = len(coefficients)
    len_prices = len(market_prices)

    if not len_prices == len_coefficients:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error in generating orders, the number "
                                                                            "of prices and the number of coefficients "
                                                                            "don't match")

    print(portfolio_service.pairs)
    print(portfolio_service.portfolio)
    print(portfolio_service.pairs_info)

    timestamp = int(time.time() * 1000)

    try:
        for i in range(len_prices):
            print(coefficients[i], market_prices[i])
            order = client.create_order(symbol=order_dict["asset"],
                                        side=order_dict["side"],
                                        type="LIMIT",
                                        timeInForce="GTC",
                                        quantity=round(coefficients[i], 2),
                                        price=round(market_prices[i], 2),
                                        recvWindow=settings.recv_window,
                                        timestamp=timestamp)
            print(order)

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return {"message": "Order(s) placed successfully"}
