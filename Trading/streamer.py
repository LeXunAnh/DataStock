import websocket
import json
# import config
from ssi_fc_data.fc_md_stream import MarketDataStream
from ssi_fc_data.fc_md_client import MarketDataClient


class MarketCollector:
    def __init__(self, config, channel):
        # self.db = DatabaseHandler()
        self.config = config
        self.channel = channel
        self.mm = MarketDataStream(config, MarketDataClient(config))

    def get_market_data(self, message):
        try:
            data = json.loads(message)
            print("Received:", data)

            row = {
                "symbol": data.get("symbol"),
                "price": data.get("price"),
                "volume": data.get("volume"),
                "ts": data.get("ts")
            }
            self.db.insert_market_data(row)

        except Exception as e:
            print("Error processing message:", e)

    def get_error(self, error):
        print("Error:", error)

    def start(self):
        print(f"🚀 Starting collector on channel: {self.channel}")
        self.mm.start(self.get_market_data, self.get_error, self.channel)

        # interactive channel switching
        message = None
        while message != "exit()":
            message = input(">> ")
            if message and message != "exit()":
                self.mm.swith_channel(message)

