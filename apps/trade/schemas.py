from typing import Union

from pydantic import BaseModel


class AccountBalance(BaseModel):
    asset: Union[str, None] = None
    free: Union[float, None] = None
    locked: Union[float, None] = None


class OrderSchema(BaseModel):
    asset: Union[str, None] = None
    volume: Union[float, None] = None
    number: Union[int, None] = None
    amountDif: Union[float, None] = None
    side: Union[str, None] = "SELL"
    priceMin: Union[float, None] = None
    priceMax: Union[float, None] = None


class ExchangeRateSchema(BaseModel):
    pair: Union[str, None] = None
    rate: Union[float, None] = None


class OrderListSchema(BaseModel):
    symbol: Union[str, None] = None
    orderId: Union[int, None] = None
    orderListId: Union[int, None] = None
    clientOrderId: Union[str, None] = None
    price: Union[float, None] = None
    origQty: Union[float, None] = None
    executedQty: Union[float, None] = None
    cummulativeQuoteQty: Union[float, None] = None
    status: Union[str, None] = None
    timeInForce: Union[str, None] = None
    type: Union[str, None] = None
    side: Union[str, None] = None
    stopPrice: Union[float, None] = None
    icebergQty: Union[float, None] = None
    time: Union[int, None] = None
    updateTime: Union[int, None] = None
    isWorking: Union[bool, None] = None
    origQuoteOrderQty: Union[float, None] = None
    selfTradePrevention: Union[str, None] = None

