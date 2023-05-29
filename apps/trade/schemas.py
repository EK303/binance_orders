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
