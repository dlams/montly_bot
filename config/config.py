from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

TOKEN_KEY = "TOKEN"

def get_discord_token():
    return os.getenv(TOKEN_KEY)