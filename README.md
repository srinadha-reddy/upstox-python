# Upstox Python SDK for API v2

![PyPI](https://img.shields.io/pypi/v/upstox-python-sdk?label=upstox-python-sdk)

## Introduction

The official Python client for communicating with the <a href="https://upstox.com/uplink/">Upstox API</a>.

Upstox API is a set of rest APIs that provide data required to build a complete investment and trading platform. Execute orders in real time, manage user portfolio, stream live market data (using Websocket), and more, with the easy to understand API collection. 

- API version: v2
- Package version: 2.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project.

## Documentation.

<a href="https://upstox.com/developer/api-documentation">Upstox API Documentation</a>

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install upstox-python-sdk
```
(you may need to run `pip` with root permission: `sudo pip install upstox-python-sdk`)

Then import the package:
```python
import upstox_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import upstox_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import upstox_client
from upstox_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAUTH2
configuration = upstox_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = upstox_client.ChargeApi(upstox_client.ApiClient(configuration))
instrument_token = 'instrument_token_example' # str | Key of the instrument
quantity = 56 # int | Quantity with which the order is to be placed
product = 'product_example' # str | Product with which the order is to be placed
transaction_type = 'transaction_type_example' # str | Indicates whether its a BUY or SELL order
price = 3.4 # float | Price with which the order is to be placed
api_version = 'api_version_example' # str | API Version Header

try:
    # Brokerage details
    api_response = api_instance.get_brokerage(instrument_token, quantity, product, transaction_type, price, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargeApi->get_brokerage: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api-v2.upstox.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ChargeApi* | [**get_brokerage**](docs/ChargeApi.md#get_brokerage) | **GET** /charges/brokerage | Brokerage details
*HistoryApi* | [**get_historical_candle_data**](docs/HistoryApi.md#get_historical_candle_data) | **GET** /historical-candle/{instrumentKey}/{interval}/{to_date} | Historical candle data
*HistoryApi* | [**get_historical_candle_data1**](docs/HistoryApi.md#get_historical_candle_data1) | **GET** /historical-candle/{instrumentKey}/{interval}/{to_date}/{from_date} | Historical candle data
*HistoryApi* | [**get_intra_day_candle_data**](docs/HistoryApi.md#get_intra_day_candle_data) | **GET** /historical-candle/intraday/{instrumentKey}/{interval} | Intra day candle data
*LoginApi* | [**authorize**](docs/LoginApi.md#authorize) | **GET** /login/authorization/dialog | Authorize API
*LoginApi* | [**logout**](docs/LoginApi.md#logout) | **DELETE** /logout | Logout
*LoginApi* | [**token**](docs/LoginApi.md#token) | **POST** /login/authorization/token | Get token API
*MarketQuoteApi* | [**get_full_market_quote**](docs/MarketQuoteApi.md#get_full_market_quote) | **GET** /market-quote/quotes | Market quotes and instruments - Full market quotes
*MarketQuoteApi* | [**get_market_quote_ohlc**](docs/MarketQuoteApi.md#get_market_quote_ohlc) | **GET** /market-quote/ohlc | Market quotes and instruments - OHLC quotes
*MarketQuoteApi* | [**ltp**](docs/MarketQuoteApi.md#ltp) | **GET** /market-quote/ltp | Market quotes and instruments - LTP quotes.
*OrderApi* | [**cancel_order**](docs/OrderApi.md#cancel_order) | **DELETE** /order/cancel | Cancel order
*OrderApi* | [**get_order_book**](docs/OrderApi.md#get_order_book) | **GET** /order/retrieve-all | Get order book
*OrderApi* | [**get_order_details**](docs/OrderApi.md#get_order_details) | **GET** /order/history | Get order details
*OrderApi* | [**get_trade_history**](docs/OrderApi.md#get_trade_history) | **GET** /order/trades/get-trades-for-day | Get trades
*OrderApi* | [**get_trades_by_order**](docs/OrderApi.md#get_trades_by_order) | **GET** /order/trades | Get trades for order
*OrderApi* | [**modify_order**](docs/OrderApi.md#modify_order) | **PUT** /order/modify | Modify order
*OrderApi* | [**place_order**](docs/OrderApi.md#place_order) | **POST** /order/place | Place order
*PortfolioApi* | [**convert_positions**](docs/PortfolioApi.md#convert_positions) | **PUT** /portfolio/convert-position | Convert Positions
*PortfolioApi* | [**get_holdings**](docs/PortfolioApi.md#get_holdings) | **GET** /portfolio/long-term-holdings | Get Holdings
*PortfolioApi* | [**get_positions**](docs/PortfolioApi.md#get_positions) | **GET** /portfolio/short-term-positions | Get Positions
*TradeProfitAndLossApi* | [**get_profit_and_loss_charges**](docs/TradeProfitAndLossApi.md#get_profit_and_loss_charges) | **GET** /trade/profit-loss/charges | Get profit and loss on trades
*TradeProfitAndLossApi* | [**get_trade_wise_profit_and_loss_data**](docs/TradeProfitAndLossApi.md#get_trade_wise_profit_and_loss_data) | **GET** /trade/profit-loss/data | Get Trade-wise Profit and Loss Report Data
*TradeProfitAndLossApi* | [**get_trade_wise_profit_and_loss_meta_data**](docs/TradeProfitAndLossApi.md#get_trade_wise_profit_and_loss_meta_data) | **GET** /trade/profit-loss/metadata | Get profit and loss meta data on trades
*UserApi* | [**get_profile**](docs/UserApi.md#get_profile) | **GET** /user/profile | Get profile
*UserApi* | [**get_user_fund_margin**](docs/UserApi.md#get_user_fund_margin) | **GET** /user/get-funds-and-margin | Get User Fund And Margin
*WebsocketApi* | [**get_market_data_feed**](docs/WebsocketApi.md#get_market_data_feed) | **GET** /feed/market-data-feed | Market Data Feed
*WebsocketApi* | [**get_market_data_feed_authorize**](docs/WebsocketApi.md#get_market_data_feed_authorize) | **GET** /feed/market-data-feed/authorize | Market Data Feed Authorize
*WebsocketApi* | [**get_portfolio_stream_feed**](docs/WebsocketApi.md#get_portfolio_stream_feed) | **GET** /feed/portfolio-stream-feed | Portfolio Stream Feed
*WebsocketApi* | [**get_portfolio_stream_feed_authorize**](docs/WebsocketApi.md#get_portfolio_stream_feed_authorize) | **GET** /feed/portfolio-stream-feed/authorize | Portfolio Stream Feed Authorize

## Documentation For Models

 - [ApiGatewayErrorResponse](docs/ApiGatewayErrorResponse.md)
 - [BrokerageData](docs/BrokerageData.md)
 - [BrokerageTaxes](docs/BrokerageTaxes.md)
 - [BrokerageWrapperData](docs/BrokerageWrapperData.md)
 - [CancelOrderData](docs/CancelOrderData.md)
 - [CancelOrderResponse](docs/CancelOrderResponse.md)
 - [ConvertPositionData](docs/ConvertPositionData.md)
 - [ConvertPositionRequest](docs/ConvertPositionRequest.md)
 - [ConvertPositionResponse](docs/ConvertPositionResponse.md)
 - [Depth](docs/Depth.md)
 - [DepthMap](docs/DepthMap.md)
 - [DpPlan](docs/DpPlan.md)
 - [GetBrokerageResponse](docs/GetBrokerageResponse.md)
 - [GetFullMarketQuoteResponse](docs/GetFullMarketQuoteResponse.md)
 - [GetHistoricalCandleResponse](docs/GetHistoricalCandleResponse.md)
 - [GetHoldingsResponse](docs/GetHoldingsResponse.md)
 - [GetIntraDayCandleResponse](docs/GetIntraDayCandleResponse.md)
 - [GetMarketQuoteLastTradedPriceResponse](docs/GetMarketQuoteLastTradedPriceResponse.md)
 - [GetMarketQuoteOHLCResponse](docs/GetMarketQuoteOHLCResponse.md)
 - [GetOrderBookResponse](docs/GetOrderBookResponse.md)
 - [GetOrderResponse](docs/GetOrderResponse.md)
 - [GetPositionResponse](docs/GetPositionResponse.md)
 - [GetProfileResponse](docs/GetProfileResponse.md)
 - [GetProfitAndLossChargesResponse](docs/GetProfitAndLossChargesResponse.md)
 - [GetTradeResponse](docs/GetTradeResponse.md)
 - [GetTradeWiseProfitAndLossDataResponse](docs/GetTradeWiseProfitAndLossDataResponse.md)
 - [GetTradeWiseProfitAndLossMetaDataResponse](docs/GetTradeWiseProfitAndLossMetaDataResponse.md)
 - [GetUserFundMarginResponse](docs/GetUserFundMarginResponse.md)
 - [HistoricalCandleData](docs/HistoricalCandleData.md)
 - [HoldingsData](docs/HoldingsData.md)
 - [IntraDayCandleData](docs/IntraDayCandleData.md)
 - [LogoutResponse](docs/LogoutResponse.md)
 - [MarketQuoteOHLC](docs/MarketQuoteOHLC.md)
 - [MarketQuoteSymbol](docs/MarketQuoteSymbol.md)
 - [MarketQuoteSymbolLtp](docs/MarketQuoteSymbolLtp.md)
 - [ModifyOrderData](docs/ModifyOrderData.md)
 - [ModifyOrderRequest](docs/ModifyOrderRequest.md)
 - [ModifyOrderResponse](docs/ModifyOrderResponse.md)
 - [OAuthClientException](docs/OAuthClientException.md)
 - [OAuthClientExceptionCause](docs/OAuthClientExceptionCause.md)
 - [OAuthClientExceptionCauseStackTrace](docs/OAuthClientExceptionCauseStackTrace.md)
 - [OAuthClientExceptionCauseSuppressed](docs/OAuthClientExceptionCauseSuppressed.md)
 - [Ohlc](docs/Ohlc.md)
 - [OrderBookData](docs/OrderBookData.md)
 - [OrderData](docs/OrderData.md)
 - [OtherTaxes](docs/OtherTaxes.md)
 - [PlaceOrderData](docs/PlaceOrderData.md)
 - [PlaceOrderRequest](docs/PlaceOrderRequest.md)
 - [PlaceOrderResponse](docs/PlaceOrderResponse.md)
 - [PositionData](docs/PositionData.md)
 - [Problem](docs/Problem.md)
 - [ProfileData](docs/ProfileData.md)
 - [ProfitAndLossChargesData](docs/ProfitAndLossChargesData.md)
 - [ProfitAndLossChargesTaxes](docs/ProfitAndLossChargesTaxes.md)
 - [ProfitAndLossChargesWrapperData](docs/ProfitAndLossChargesWrapperData.md)
 - [ProfitAndLossMetaData](docs/ProfitAndLossMetaData.md)
 - [ProfitAndLossMetaDataWrapper](docs/ProfitAndLossMetaDataWrapper.md)
 - [ProfitAndLossOtherChargesTaxes](docs/ProfitAndLossOtherChargesTaxes.md)
 - [TokenRequest](docs/TokenRequest.md)
 - [TokenResponse](docs/TokenResponse.md)
 - [TradeData](docs/TradeData.md)
 - [TradeWiseMetaData](docs/TradeWiseMetaData.md)
 - [TradeWiseProfitAndLossData](docs/TradeWiseProfitAndLossData.md)
 - [UserFundMarginData](docs/UserFundMarginData.md)
 - [WebsocketAuthRedirectResponse](docs/WebsocketAuthRedirectResponse.md)
 - [WebsocketAuthRedirectResponseData](docs/WebsocketAuthRedirectResponseData.md)
