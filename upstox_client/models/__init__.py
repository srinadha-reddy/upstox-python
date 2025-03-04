# coding: utf-8

# flake8: noqa
"""
    Upstox Developer API

    Build your App on the Upstox platform  ![Banner](https://api-v2.upstox.com/api-docs/images/banner.jpg \"banner\")  # Introduction  Upstox API is a set of rest APIs that provide data required to build a complete investment and trading platform. Execute orders in real time, manage user portfolio, stream live market data (using Websocket), and more, with the easy to understand API collection.  All requests are over HTTPS and the requests are sent with the content-type ‘application/json’. Developers have the option of choosing the response type as JSON or CSV for a few API calls.  To be able to use these APIs you need to create an App in the Developer Console and generate your **apiKey** and **apiSecret**. You can use a redirect URL which will be called after the login flow.  If you are a **trader**, you can directly create apps from Upstox mobile app or the desktop platform itself from **Apps** sections inside the **Account** Tab. Head over to <a href=\"http://account.upstox.com/developer/apps\" target=\"_blank\">account.upstox.com/developer/apps</a>.</br> If you are a **business** looking to integrate Upstox APIs, reach out to us and we will get a custom app created for you in no time.  It is highly recommended that you do not embed the **apiSecret** in your frontend app. Create a remote backend which does the handshake on behalf of the frontend app. Marking the apiSecret in the frontend app will make your app vulnerable to threats and potential issues.   # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from upstox_client.models.analytics_data import AnalyticsData
from upstox_client.models.api_gateway_error_response import ApiGatewayErrorResponse
from upstox_client.models.batch_execution_summary import BatchExecutionSummary
from upstox_client.models.brokerage_data import BrokerageData
from upstox_client.models.brokerage_taxes import BrokerageTaxes
from upstox_client.models.brokerage_wrapper_data import BrokerageWrapperData
from upstox_client.models.cancel_or_exit_multi_order_data import CancelOrExitMultiOrderData
from upstox_client.models.cancel_or_exit_multi_order_response import CancelOrExitMultiOrderResponse
from upstox_client.models.cancel_or_exit_order_error_data import CancelOrExitOrderErrorData
from upstox_client.models.cancel_order_data import CancelOrderData
from upstox_client.models.cancel_order_response import CancelOrderResponse
from upstox_client.models.cancel_order_v3_response import CancelOrderV3Response
from upstox_client.models.convert_position_data import ConvertPositionData
from upstox_client.models.convert_position_request import ConvertPositionRequest
from upstox_client.models.convert_position_response import ConvertPositionResponse
from upstox_client.models.depth import Depth
from upstox_client.models.depth_map import DepthMap
from upstox_client.models.dp_plan import DpPlan
from upstox_client.models.exchange_timing_data import ExchangeTimingData
from upstox_client.models.get_brokerage_response import GetBrokerageResponse
from upstox_client.models.get_exchange_timing_response import GetExchangeTimingResponse
from upstox_client.models.get_full_market_quote_response import GetFullMarketQuoteResponse
from upstox_client.models.get_gtt_order_response import GetGttOrderResponse
from upstox_client.models.get_historical_candle_response import GetHistoricalCandleResponse
from upstox_client.models.get_holdings_response import GetHoldingsResponse
from upstox_client.models.get_holiday_response import GetHolidayResponse
from upstox_client.models.get_intra_day_candle_response import GetIntraDayCandleResponse
from upstox_client.models.get_market_quote_last_traded_price_response import GetMarketQuoteLastTradedPriceResponse
from upstox_client.models.get_market_quote_ohlc_response import GetMarketQuoteOHLCResponse
from upstox_client.models.get_market_status_response import GetMarketStatusResponse
from upstox_client.models.get_option_chain_response import GetOptionChainResponse
from upstox_client.models.get_option_contract_response import GetOptionContractResponse
from upstox_client.models.get_order_book_response import GetOrderBookResponse
from upstox_client.models.get_order_details_response import GetOrderDetailsResponse
from upstox_client.models.get_order_response import GetOrderResponse
from upstox_client.models.get_position_response import GetPositionResponse
from upstox_client.models.get_profile_response import GetProfileResponse
from upstox_client.models.get_profit_and_loss_charges_response import GetProfitAndLossChargesResponse
from upstox_client.models.get_trade_response import GetTradeResponse
from upstox_client.models.get_trade_wise_profit_and_loss_data_response import GetTradeWiseProfitAndLossDataResponse
from upstox_client.models.get_trade_wise_profit_and_loss_meta_data_response import GetTradeWiseProfitAndLossMetaDataResponse
from upstox_client.models.get_user_fund_margin_response import GetUserFundMarginResponse
from upstox_client.models.gtt_cancel_order_request import GttCancelOrderRequest
from upstox_client.models.gtt_modify_order_request import GttModifyOrderRequest
from upstox_client.models.gtt_order_data import GttOrderData
from upstox_client.models.gtt_order_details import GttOrderDetails
from upstox_client.models.gtt_place_order_request import GttPlaceOrderRequest
from upstox_client.models.gtt_rule import GttRule
from upstox_client.models.gtt_trigger_order_response import GttTriggerOrderResponse
from upstox_client.models.historical_candle_data import HistoricalCandleData
from upstox_client.models.holdings_data import HoldingsData
from upstox_client.models.holiday_data import HolidayData
from upstox_client.models.indie_user_init_token_data import IndieUserInitTokenData
from upstox_client.models.indie_user_init_token_response import IndieUserInitTokenResponse
from upstox_client.models.indie_user_token_request import IndieUserTokenRequest
from upstox_client.models.instrument import Instrument
from upstox_client.models.instrument_data import InstrumentData
from upstox_client.models.intra_day_candle_data import IntraDayCandleData
from upstox_client.models.logout_response import LogoutResponse
from upstox_client.models.margin import Margin
from upstox_client.models.margin_data import MarginData
from upstox_client.models.margin_request import MarginRequest
from upstox_client.models.market_data import MarketData
from upstox_client.models.market_quote_ohlc import MarketQuoteOHLC
from upstox_client.models.market_quote_symbol import MarketQuoteSymbol
from upstox_client.models.market_quote_symbol_ltp import MarketQuoteSymbolLtp
from upstox_client.models.market_status_data import MarketStatusData
from upstox_client.models.modify_order_data import ModifyOrderData
from upstox_client.models.modify_order_request import ModifyOrderRequest
from upstox_client.models.modify_order_response import ModifyOrderResponse
from upstox_client.models.modify_order_v3_response import ModifyOrderV3Response
from upstox_client.models.multi_order_data import MultiOrderData
from upstox_client.models.multi_order_error import MultiOrderError
from upstox_client.models.multi_order_request import MultiOrderRequest
from upstox_client.models.multi_order_response import MultiOrderResponse
from upstox_client.models.multi_order_summary import MultiOrderSummary
from upstox_client.models.multi_order_v3_data import MultiOrderV3Data
from upstox_client.models.o_auth_client_exception import OAuthClientException
from upstox_client.models.o_auth_client_exception_cause import OAuthClientExceptionCause
from upstox_client.models.o_auth_client_exception_cause_stack_trace import OAuthClientExceptionCauseStackTrace
from upstox_client.models.o_auth_client_exception_cause_suppressed import OAuthClientExceptionCauseSuppressed
from upstox_client.models.ohlc import Ohlc
from upstox_client.models.option_strike_data import OptionStrikeData
from upstox_client.models.order_book_data import OrderBookData
from upstox_client.models.order_data import OrderData
from upstox_client.models.order_metadata import OrderMetadata
from upstox_client.models.other_taxes import OtherTaxes
from upstox_client.models.place_order_data import PlaceOrderData
from upstox_client.models.place_order_request import PlaceOrderRequest
from upstox_client.models.place_order_response import PlaceOrderResponse
from upstox_client.models.place_order_v3_request import PlaceOrderV3Request
from upstox_client.models.place_order_v3_response import PlaceOrderV3Response
from upstox_client.models.position_data import PositionData
from upstox_client.models.post_margin_response import PostMarginResponse
from upstox_client.models.problem import Problem
from upstox_client.models.profile_data import ProfileData
from upstox_client.models.profit_and_loss_charges_data import ProfitAndLossChargesData
from upstox_client.models.profit_and_loss_charges_taxes import ProfitAndLossChargesTaxes
from upstox_client.models.profit_and_loss_charges_wrapper_data import ProfitAndLossChargesWrapperData
from upstox_client.models.profit_and_loss_meta_data import ProfitAndLossMetaData
from upstox_client.models.profit_and_loss_meta_data_wrapper import ProfitAndLossMetaDataWrapper
from upstox_client.models.profit_and_loss_other_charges_taxes import ProfitAndLossOtherChargesTaxes
from upstox_client.models.put_call_option_chain_data import PutCallOptionChainData
from upstox_client.models.rule import Rule
from upstox_client.models.token_request import TokenRequest
from upstox_client.models.token_response import TokenResponse
from upstox_client.models.trade_data import TradeData
from upstox_client.models.trade_history_response import TradeHistoryResponse
from upstox_client.models.trade_history_response_meta_data import TradeHistoryResponseMetaData
from upstox_client.models.trade_history_response_page_data import TradeHistoryResponsePageData
from upstox_client.models.trade_history_response_trade_data import TradeHistoryResponseTradeData
from upstox_client.models.trade_wise_meta_data import TradeWiseMetaData
from upstox_client.models.trade_wise_profit_and_loss_data import TradeWiseProfitAndLossData
from upstox_client.models.user_fund_margin_data import UserFundMarginData
from upstox_client.models.websocket_auth_redirect_response import WebsocketAuthRedirectResponse
from upstox_client.models.websocket_auth_redirect_response_data import WebsocketAuthRedirectResponseData
