import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "http://open-api.bybt.com"
OI_URL = "{}/api/pro/v1/futures/openInterest".format(BASE_URL)
OI_CHART_URL = "{}/api/pro/v1/futures/openInterest/chart".format(BASE_URL)
LIQUIDATION_CHART_URL = "{}/api/pro/v1/futures/liquidation_chart".format(BASE_URL)
LONG_SHORT_URL = "{}/api/pro/v1/futures/longShort_chart".format(BASE_URL)
FUNDING_CHART_URL = "{}/api/pro/v1/futures/funding_rates_chart".format(BASE_URL)
NEWEST_FUNDING_URL = "{}/api/pro/v1/futures/funding_rates".format(BASE_URL)
EXCHANGE_URL = "{}/api/pro/v1/futures/vol/chart".format(BASE_URL)
OPTIONS_OI_URL = "{}/api/pro/v1/option/openInterest".format(BASE_URL)
OPTIONS_OI_CHART_URL = "{}/api/pro/v1/option/openInterest/history/chart".format(BASE_URL)
OPTIONS_EXCHANGE_VOL_URL = "{}/api/pro/v1/option/vol/history/chart".format(BASE_URL)

headers = {
    "bybtSecret": os.getenv("BYBT_API_KEY")
}

# interval: ALL: 0, 1H: 2, 4H: 1, 12H: 4, 24H: 5
# symbol: eg. "BTC"
def get_OI(interval, symbol):
    r = requests.get(OI_URL, headers=headers, params={"interval": interval,"symbol": symbol})

    return json.loads(r.content)

# interval: ALL: 0, 1H: 2, 4H: 1, 12H: 4, 24H: 5
# symbol: eg. "BTC"
def get_OI_chart(interval, symbol):
    r = requests.get(OI_CHART_URL, headers=headers, params={"interval": interval,"symbol": symbol})

    return json.loads(r.content)

# exName: Exchange Name eg. "Binance"
# symbol: eg. "BTC"
def get_liquidation_chart(exName=None, symbol=None):
    r = requests.get(LIQUIDATION_CHART_URL, headers=headers, params={"exName": exName,"symbol": symbol,})

    return json.loads(r.content)

# interval: 1H:2, 4H:1, 12H:4, 24H:5
# symbol: eg. "BTC"
def get_long_short_ratio(interval, symbol):
    r = requests.get(LONG_SHORT_URL, headers=headers, params={"interval": interval, "symbol": symbol})

    return json.loads(r.content)

# symbol: eg. "BTC"
# margin_type: "C"=Token Margined, "U"=USDT or USD Margined. default C
def get_funding_chart(symbol, margin_type=None):
    r = requests.get(FUNDING_CHART_URL, headers=headers, params={"type": margin_type, "symbol": symbol})

    return json.loads(r.content)

# symbol: if this parameter is not passed, all symbol are returned (eg. "BTC")
def get_newest_funding(symbol=None): 
    r = requests.get(NEWEST_FUNDING_URL, headers=headers, params={"symbol": symbol})

    return json.loads(r.content)

# symbol: eg. "BTC"
def get_exchange_volume(symbol):
    r = requests.get(EXCHANGE_URL, headers=headers, params={"symbol": symbol})

    return json.loads(r.content)

# authentication: Authentication token to track down who is emptying our stocks.
# symbol: eg. "BTC"
def get_options_OI(authentication, symbol):
     r = requests.get(EXCHANGE_URL, headers=headers, params={"authentication": authentication, "symbol": symbol})

     return json.loads(r.content)

# interval: All:0, 1H:2, 4H:1, 12H:4, 24H:5
# symbol: eg. "BTC"
def get_options_OI_chart(interval, symbol):
     r = requests.get(OPTIONS_OI_CHART_URL, headers=headers, params={"interval": interval, "symbol": symbol})

     return json.loads(r.content)

# symbol: eg. "BTC"
def get_options_exchange_vol(symbol):
     r = requests.get(OPTIONS_EXCHANGE_VOL_URL, headers=headers, params={"symbol": symbol})

     return json.loads(r.content)
