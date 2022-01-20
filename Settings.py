from dotenv import load_dotenv
from pathlib import Path
import os


load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_HOST = os.getenv("DATABASE_HOST")

WORDLIST_PERINTAH = os.getenv("WORDLIST_PERINTAH")
WORDLIST_STOPWORD = os.getenv("WORDLIST_STOPWORD")
WORDLIST_KONDISI = os.getenv("WORDLIST_KONDISI")
WORDLIST_SIMBOL = os.getenv("WORDLIST_SIMBOL")
