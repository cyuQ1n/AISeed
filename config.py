import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# App Settings
APP_NAME = "LLM QA API"
APP_VERSION = "0.1.0"
APP_DESCRIPTION = "A simple API for LLM-based question answering"

# API Documentation config
DOCS_URL = "/docs"
REDOC_URL = "/redoc"
OPENAPI_URL = "/openapi.json"

# Server Settings
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8989))

# OpenAI API Settings
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "Qwen/Qwen2.5-7B-Instruct")
API_BASE = os.getenv("API_BASE", "https://api.siliconflow.cn/v1")
API_KEY = os.getenv("API_KEY", "sk-uvdrjdsqmrurkcdwqralhbnsubcnllxikryzoxrvrckpydxm")

# API Request Settings
MAX_RETRIES = 3
RETRY_DELAY = 1
DEFAULT_TEMPERATURE = 0.7