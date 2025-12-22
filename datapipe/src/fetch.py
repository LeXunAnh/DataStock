import json
import pandas as pd
from ssi_fc_data import fc_md_client, model
from dotenv import load_dotenv
import os
from datapipe.src.db import get_connection, close_connection
from datapipe.config import config
from vnstock import Company
import time
client = fc_md_client.MarketDataClient(config)


#extract data
def fetch_data_ohlc_daily(symbol, time_start, time_end):
    data = client.daily_ohlc(config, model.daily_ohlc(symbol, time_start, time_end, 1, 9999, True))
    data = data.get("data", [])
    return pd.DataFrame(data)
    #return data

def fetch_securities_hose(market = "hose"):
    data = client.securities(config, model.securities(market, 1, 1000))
    stock_list = data.get("data", [])
    return pd.DataFrame(stock_list)

def fetch_securities_hnx(market = "hnx"):
    data = client.securities(config, model.securities(market, 1, 1000))
    stock_list = data.get("data", [])
    return pd.DataFrame(stock_list)

def fetch_intraday_stock_price(symbol, time_start, time_end, market = "hose"):
    data = client.intraday_ohlc(config, model.intraday_ohlc(symbol, time_start, time_end, 1, 1000,market))
    return data

def get_info_sercurities(symbol):
    company = Company(symbol=symbol, source='VCI')
    max_retries = 20  # Maximum number of retries
    for attempt in range(max_retries):
        try:
            df = company.overview()
            df2 = df[["symbol", "icb_name2"]]
            return df2
        except Exception as e:
            print(f"Error occurred: {e}. Retrying in 10 seconds...")
            time.sleep(10)  # Wait for 10 seconds before retrying
    return None  # Return None if all retries fail

def save_to_json(data_dict):
    datafile = 'stockdata.json'
    with open(datafile, 'w') as json_file:
        json.dump(data_dict, json_file, indent=1)
    print(f"All symbols data saved to {datafile}")
