"""
Configuration module for loading environment variables required for API access.
"""
import dotenv
import os

dotenv.load_dotenv()

BASE_URL = os.getenv("BASE_URL")
USERNAME = os.getenv("LUMEN_USERNAME")
PASSWORD = os.getenv("PASSWORD")