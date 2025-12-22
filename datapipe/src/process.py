from datetime import datetime
import pandas as pd

def get_all_symbols(conn):
    cursor = conn.cursor()
    #cursor.execute("SELECT symbol FROM stock_list")
    #cursor.execute("SELECT symbol FROM stock_list WHERE LENGTH(symbol) = 3")
    cursor.execute("""
            SELECT symbol FROM stock_list
            WHERE market = 'HOSE' AND LENGTH(symbol) = 3
        """)
    symbols = [row[0] for row in cursor.fetchall()]
    cursor.close()
    return symbols

def insert_stock_industry(df,conn):
    cursor = conn.cursor()
    insert_query ="""
        INSERT INTO stock_industry (symbol, industry_name) 
        VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE 
        industry_name = VALUES(industry_name);
    """
    for _, row in df.iterrows():
        values = (
            row["symbol"],
            row["icb_name2"]
        )
        try:
            cursor.execute(insert_query, values)
        except Exception as e:
            print(f"❌ Error inserting row {values}: {e}")

    conn.commit()
    cursor.close()

def insert_stock_list(df, conn):
    cursor = conn.cursor()

    insert_query = """
        INSERT INTO stock_list (symbol, market, stock_name, stock_enname)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            market=VALUES(market),
            stock_name=VALUES(stock_name),
            stock_enname=VALUES(stock_enname);
    """

    for _, row in df.iterrows():
        values = (
            row["Symbol"],
            row["Market"],
            row["StockName"],
            row["StockEnName"]
        )
        try:
            cursor.execute(insert_query, values)
        except Exception as e:
            print(f"❌ Error inserting row {values}: {e}")

    conn.commit()
    cursor.close()
    print("✅ Stock list inserted/updated.")


def insert_ohlc_data(df, conn):
    cursor = conn.cursor()

    insert_query = """
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
                int(float(row["Value"]))
            )
            cursor.execute(insert_query, values)

        except Exception as e:
            print(f"❌ Error inserting OHLC for {row.get('Symbol')}: {e}")

    conn.commit()
    cursor.close()
