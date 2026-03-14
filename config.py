# config.py

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'
    DEBUG = os.environ.get('DEBUG', default=False)
    # API keys
    API_KEY = os.environ.get('API_KEY')
    ANOTHER_API_KEY = os.environ.get('ANOTHER_API_KEY')
