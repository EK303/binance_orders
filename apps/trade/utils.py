from .service import Result, PortfolioService

portfolio_service = PortfolioService.get_instance()


def check_order(asset: str,
                volume: float,
                number: int,
                amountDif: float,
                side: str,
                priceMin: float,
                priceMax: float) -> Result:

    if not asset in portfolio_service.pairs:
        return Result.fail(status=False, message="The pair is not in the list of trades")

    if not number:
        return Result.fail(status=False, message="Number of orders is required")

    if not amountDif:
        amountDif = 0

    if not side in ["SELL", "BUY"]:
        return Result.fail(status=False, message="Invalid side")

    if not priceMin:
        return Result.fail(status=False, message="Minimum price is required")

    if not priceMax:
        return Result.fail(status=False, message="Maximum price is required")

    return Result.success(status=True, data=None)


def get_exchange_rate(pair: str):
    for pair_info in portfolio_service.pairs_info:
        if pair_info["pair"] == pair:
            return Result.success(status=True, data=pair_info["rate"])
    return Result.fail(status=False, message="The exchange rate is not found")


def get_min_qty(pair: str):
    for pair_info in portfolio_service.quotes_info:
        if pair_info["symbol"] == pair:
            for fil in pair_info["filters"]:
                if fil["filterType"] == "LOT_SIZE":
                    min_qty = float(fil["minQty"])
                    min_qty = len(str(min_qty)) - 2
                    return Result.success(status=True, data=min_qty)

    return Result.fail(status=False, message="The minQty is not found")

