import json
import pandas as pd
from ssi_fc_data import fc_md_client, model
from vnstock import Company
import time


class DataAPI:
    def __init__(self, config):
        self.config = config
        self.client = fc_md_client.MarketDataClient(self.config)

    def get_securities(self, market="hose"):
        try:
            data = self.client.securities(
                self.config,
                model.securities(market, 1, 1000)
            )
            stock_list = data.get("data", [])
            return pd.DataFrame(stock_list)
        except Exception as e:
            print(f"Error fetching securities for {market}: {e}")
            return pd.DataFrame()

    def get_data_ohlc_daily(self, symbol, time_start, time_end):
        try:
            data = self.client.daily_ohlc(
                self.config,
                model.daily_ohlc(symbol, time_start, time_end, 1, 9999, True)
            )
            data = data.get("data", [])
            return pd.DataFrame(data)
        except Exception as e:
            print(f"Error fetching OHLC data for {symbol}: {e}")
            return pd.DataFrame()

    def get_intraday_stock_price(self, symbol, time_start, time_end, market="hose"):
        try:
            data = self.client.intraday_ohlc(
                self.config,
                model.intraday_ohlc(symbol, time_start, time_end, 1, 1000, market)
            )
            return data
        except Exception as e:
            print(f"Error fetching intraday data for {symbol}: {e}")
            return {}

