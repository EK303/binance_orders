from apps.config import settings

client = settings.TESTNET_CLIENT


class Result:

    def __init__(self, *args, **kwargs):
        self.status = kwargs.get("status", None)
        self.message = kwargs.get("message", None)
        self.data = kwargs.get("data", None)
        self.amount_dif = kwargs.get("amount_dif", None)

    @classmethod
    def success(cls, *args, **kwargs):
        return cls(*args, **kwargs)

    @classmethod
    def fail(cls, *args, **kwargs):
        return cls(*args, **kwargs)


# can instantiate only one object of this class to help track operations with assets
class PortfolioService:
    """
    tickers: a set consisting all the tickers currently held by the user
    portfolio: a list of dictionaries consisting all the assets held by the user and respective balances
    """

    tickers: set = {}
    portfolio: list = []
    pairs: set = {}

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._get_portfolio()
            cls._instance._get_tickers()
            cls._instance._get_pairs()
        return cls._instance

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def _get_portfolio(self):
        if not self.portfolio:
            portfolio = client.get_account()["balances"]
            self.portfolio = [{"asset": item["asset"], "free": float(item["free"]), "locked": float(item["locked"])}
                              for item in portfolio]

        return self.portfolio

    def _get_tickers(self):
        if not self.tickers:
            self.tickers = set([item["asset"] for item in self.portfolio])
        return self.tickers

    def _get_pairs(self):
        if not self.pairs:
            symbols = client.get_exchange_info()["symbols"]
            self.pairs = set([item["symbol"] for item in symbols])
        return self.pairs

    def get_pairs(self):
        return self.pairs

    def get_portfolio(self):
        return self.portfolio

    # as the positions in the portfolio are kept in plain format,
    # we avoid accounting for pairs and agree that the other side of the trade
    # by default will be USDT as the universal currency



