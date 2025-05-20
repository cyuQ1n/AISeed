import os
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Dict, Any, Optional

# Load environment variables
load_dotenv()

# Base configurations
class LLMConfig(BaseModel):
    BASE_MODEL: str
    API_BASE: str
    API_KEY: str

# Default configuration
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "Qwen/Qwen2.5-7B-Instruct")
DEFAULT_API_BASE = os.getenv("DEFAULT_API_BASE", "https://api.siliconflow.cn/v1")
DEFAULT_API_KEY = os.getenv("DEFAULT_API_KEY", "sk-uvdrjdsqmrurkcdwqralhbnsubcnllxikryzoxrvrckpydxm")

# Multiple API endpoint configurations
API_CONFIGS: Dict[str, Dict[str, str]] = {
    "local1": {
        "BASE_MODEL": "Qwen2.5-7B-Instruct",
        "API_BASE": "http://10.26.33.169:8028/v1",
        "API_KEY": "EMPTY"
    },
    "local2": {
        "BASE_MODEL": "deepseek-reasoner",
        "API_BASE": "https://api.deepseek.com/v1/",
        "API_KEY": "sk-5fd1beacfd8f4ae5bff41686beca7e3f"
    },
    "local3": {
        "BASE_MODEL": "Qwen/Qwen2.5-72B-Chat",
        "API_BASE": "https://api.siliconflow.cn/v1",
        "API_KEY": "sk-vdjlietacqqnbgsoevqfxngcrezovfhmssmypshrxoibgnud"
    },
    "local4": {
        "BASE_MODEL": "Qwen/Qwen2.5-72B-Chat",
        "API_BASE": "https://api.gpt.ge/v1/",
        "API_KEY": "sk-U3MeLOkbERfIt6781f7a7dD011B4415aB605D19602377fD7"
    },
    "local5": {
        "BASE_MODEL": "Qwen/Qwen2.5-7B-Instruct",
        "API_BASE": "http://10.26.33.169:8030/v1",
        "API_KEY": "EMPTY"
    }
}

# API Settings
MAX_RETRIES = 5
RETRY_DELAY = 1
DEFAULT_TEMPERATURE = 0.7

# Server Settings
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8989))

# App Settings
APP_NAME = "LLM QA API"
APP_VERSION = "0.1.0"
APP_DESCRIPTION = "A simple API for LLM-based question answering"
# OpenAPI Documentation config
DOCS_URL = "/docs"
REDOC_URL = "/redoc"
OPENAPI_URL = "/openapi.json" 