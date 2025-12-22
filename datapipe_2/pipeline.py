from datetime import datetime
from datapipe_2.src.dataAPI import DataAPI
from datapipe_2.src.database import Database
from datapipe_2.config import config

def update_ohlc_for_symbol(db: Database, api: DataAPI, symbol: str, from_date: str, to_date: str):
    df_ohlc = api.get_data_ohlc_daily(symbol, from_date, to_date)
    if not df_ohlc.empty:
        db.create_or_update_ohlc(df_ohlc)
        print(f"✅ OHLC data for {symbol} inserted ({from_date} → {to_date}).")
    else:
        print(f"⚠️ No OHLC data for {symbol} in range {from_date} → {to_date}.")

def update_all_ohlc(db: Database, api: DataAPI, from_date: str, to_date: str):
    symbols = db.read_symbols()
    if not symbols:
        print("⚠️ No symbols found in DB.")
        return

    for symbol in symbols:
        df_ohlc = api.get_data_ohlc_daily(symbol, from_date, to_date)
        if not df_ohlc.empty:
            db.create_or_update_ohlc(df_ohlc)
            print(f"✅ Data for {symbol} has been inserted.")
        else:
            print(f"⚠️ No OHLC data returned for {symbol}.")

def update_ohlc_daily(db: Database, api: DataAPI):
    # Use today’s date (or adjust to yesterday for EOD)
    today = datetime.today().strftime("%d/%m/%Y")

    symbols = db.read_symbols()
    if not symbols:
        print("⚠️ No symbols found in DB.")
        return

    for symbol in symbols:
        df_ohlc = api.get_data_ohlc_daily(symbol, today, today)
        if not df_ohlc.empty:
            db.create_or_update_ohlc(df_ohlc)
            print(f"✅ Daily OHLC for {symbol} updated.")
        else:
            print(f"⚠️ No OHLC data for {symbol} on {today}.")


if __name__ == "__main__":

    db = Database()
    db.connect()
    api = DataAPI(config)

    print("Select an option to run:")
    print("1. Update OHLC for specific symbol")
    print("2. Update all OHLC")
    print("3. Update OHLC daily")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        update_ohlc_for_symbol(db, api, symbol="AAA", from_date="27/08/2025", to_date="27/08/2025")
    elif choice == "2":
        update_all_ohlc(db, api, "03/09/2025", "12/12/2025")
    elif choice == "3":
        update_ohlc_daily(db, api)
    else:
        print("Invalid choice")

    # print("Done !!")
    # Close DB
    db.close()



