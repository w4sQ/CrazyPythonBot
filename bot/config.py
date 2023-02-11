from os import getenv
from pathlib import Path

servers = {
    'po3': "92.101.45.211:25565",
    'work': "194.147.90.132:25570",
    'test': "102.10.45.211:25565"
}

TELEGRAM_BOT_TOKEN = getenv("TELEGRAM_BOT_TOKEN", "")

BASE_DIR = Path(__file__).resolve().parent
SQLITE_DB_FILE = BASE_DIR / "db.sqlite3"
