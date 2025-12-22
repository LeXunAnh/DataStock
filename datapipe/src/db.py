import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Load env variables
load_dotenv(dotenv_path='config/.env')

# Function to establish MySQL connection
def get_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        if connection.is_connected():
            print("✅ Connected to MySQL")
            return connection
    except Error as e:
        print(f"❌ Error while connecting to MySQL: {e}")
        return None

# Function to close connection
def close_connection(connection):
    if connection and connection.is_connected():
        connection.close()
        print("🔌 MySQL connection closed")

