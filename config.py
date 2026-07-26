from dotenv import load_dotenv
import os

#lädt die Variablen aus der .env-Datei
load_dotenv()

APP_NAME = os.getenv("APP_NAME", "My Cloud App")
VERSION = os.getenv("APP_VERSION", "1.0.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
