from .service import Result, PortfolioService

portfolio_service = PortfolioService.get_instance()


def check_order(asset: str,
                volume: float,
                number: int,
                amountDif: float,
                side: str,
                priceMin: float,
                priceMax: float) -> Result:

    if not asset in portfolio_service.tickers:
        return Result.fail(status=False, message="Asset is not present in portfolio")

    if not number:
        return Result.fail(status=False, message="Number of orders is required")

    if not amountDif:
        return Result.fail(status=True, amount_dif=amountDif)

    if not side in ["SELL", "BUY"]:
        return Result.fail(status=False, message="Invalid side")

    if not priceMin:
        return Result.fail(status=False, message="Minimum price is required")

    if not priceMax:
        return Result.fail(status=False, message="Maximum price is required")