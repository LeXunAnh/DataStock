import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
import pandas as pd

# Load env variables
load_dotenv(dotenv_path="D:\PyFile\MarketAnalysis v0.2\datapipe_2\config\.env")

class Database:
    def __init__(self):
        self.conn = None

    # === Connection Management ===
    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                port=int(os.getenv("DB_PORT")),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME"),
            )
            if self.conn.is_connected():
                print("✅ Connected to MySQL")
        except Error as e:
            print(f"❌ Error while connecting to MySQL: {e}")
            self.conn = None
    def close(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()
            print("🔌 MySQL connection closed")

    # === CRUD Functions ===
    def read_symbols(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT symbol FROM stock_list
            WHERE market = 'HOSE' AND LENGTH(symbol) = 3
            """
        )
        symbols = [row[0] for row in cursor.fetchall()]
        cursor.close()
        return symbols

    # def create_or_update_stock_industry(self, df: pd.DataFrame):
    #     cursor = self.conn.cursor()
    #     query = """
    #         INSERT INTO stock_industry (symbol, industry_name)
    #         VALUES (%s, %s)
    #         ON DUPLICATE KEY UPDATE
    #             industry_name = VALUES(industry_name);
    #     """
    #     for _, row in df.iterrows():
    #         try:
    #             cursor.execute(query, (row["symbol"], row["icb_name2"]))
    #         except Exception as e:
    #             print(f"❌ Error inserting row {row['symbol']}: {e}")
    #     self.conn.commit()
    #     cursor.close()
    #     print("✅ Stock industry inserted/updated.")

    def create_or_update_stock_list(self, df: pd.DataFrame):
        cursor = self.conn.cursor()
        query = """
            INSERT INTO stock_list (symbol, market, stock_name, stock_enname)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                market=VALUES(market),
                stock_name=VALUES(stock_name),
                stock_enname=VALUES(stock_enname);
        """
        for _, row in df.iterrows():
            try:
                cursor.execute(
                    query,
                    (row["Symbol"], row["Market"], row["StockName"], row["StockEnName"]),
                )
            except Exception as e:
                print(f"❌ Error inserting row {row['Symbol']}: {e}")
        self.conn.commit()
        cursor.close()
        print("✅ Stock list inserted/updated.")

    def create_or_update_ohlc(self, df: pd.DataFrame):
        cursor = self.conn.cursor()
        query = """
            INSERT INTO stock_price (
                symbol, market, tradingdate, open, high, low, close, volume, value
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                open=VALUES(open),
                high=VALUES(high),
                low=VALUES(low),
                close=VALUES(close),
                volume=VALUES(volume),
                value=VALUES(value);
        """
        for _, row in df.iterrows():
            try:
                values = (
                    row["Symbol"],
                    row.get("Market", "HOSE"),
                    pd.to_datetime(row["TradingDate"], format="%d/%m/%Y").date(),
                    int(row["Open"]),
                    int(row["High"]),
                    int(row["Low"]),
                    int(row["Close"]),
                    int(float(row["Volume"])),
                    int(float(row["Value"])),
                )
                cursor.execute(query, values)
            except Exception as e:
                print(f"❌ Error inserting OHLC for {row.get('Symbol')}: {e}")
        self.conn.commit()
        cursor.close()
        print("✅ OHLC data inserted/updated.")
