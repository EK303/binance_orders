# Binance Order Placement

The application is designed to receive trade orders given the below-mentioned parameters
and placing them on the [Binance](https://www.binance.com/en) exchange in [test mode](https://testnet.binancefuture.com/en/futures/BTCUSDT)
using Binance API.

The format of parameters received is the following:

```bash
{
   "volume": 10000.0,  # Volume in USD
   "number": 5,  # Number of orders to be placed
   "amountDif": 50.0,  # Deviation in total amount between orders
   "side": "SELL",  # Trade side
   "priceMin": 200.0,  # Minimum price
   "priceMax": 300.0  # Maximum price
}
```

The application uses the **Simplex Method** from Linear Algebra to generate orders based on given constraints(parameters).

The project is going to be gradually updated and modified with additional functionality. However, at the time being, it can 
still be used to place orders, track their execution on the exchange.

The project is realized on the FastAPI Framework to save the possibilities to further expand the functionality.
Thus, the current version of the application is a simple API that receives the order parameters and places them on the exchange.

## QuickStart

Before getting the project, make sure you've [Docker](https://docs.docker.com/engine/install/) installed and configured.
To set up the application, create a project directory on your computer, navigate to it and run:

```bash
git clone git@gitlab.com:EK101/binance_orders.git
```

## Setting up Binance API

Once you've cloned from the repository, you'll need:

1) Create a .env file as per the .env_example file. If you want only test the Binance API, you can
ignore all parameters except API_KEY and API_SECRET;
2) Create a Binance account and generate API_KEY and API_SECRET in the [API Management](https://www.binance.com/en/support/faq/how-to-test-my-functions-on-binance-testnet-ab78f9a1b8824cf0a106b4229c76496d).
Once you get the get the keys set values for API_KEY and API_SECRET in the .env file.;

## Running the application

To start the application for the first time, in the root directory of the project, run the following command:

```bash
docker-compose up --build
```

To start application further usage, it's sufficient to run:

```bash
docker-compose up
```

## Usage 

As the application is set up in a testing mode, you'll be granted with an initial balance for various cryptocurrencies.
There are available endpoints that can help you track your balance, exchange rates between currencies and placed orders.

The feasible pairs for trading are as following:

```bash
"LTCBUSD", "TRXBNB", "BNBUSDT", "TRXBUSD", "LTCUSDT", "XRPBTC", "ETHUSDT", "BTCUSDT", "TRXBTC", "BNBBUSD", "BNBBTC", 
"XRPBNB", "ETHBUSD", "TRXUSDT", "BTCBUSD", "ETHBTC", "XRPBUSD", "LTCBNB", "LTCBTC", "XRPUSDT",
```
 

