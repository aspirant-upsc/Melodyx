from dotenv import load_dotenv
import os
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
OWNER_ID = int(os.getenv('OWNER_ID', '0'))
OWNER_NAME = os.getenv('OWNER_NAME', 'Owner')
FANCY_DEFAULT_PREFIX = os.getenv('FANCY_DEFAULT_PREFIX', '★')
FANCY_DEFAULT_SUFFIX = os.getenv('FANCY_DEFAULT_SUFFIX', '★')
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./melodyx_complete.db')
AI_API_KEY = os.getenv('AI_API_KEY', '')
STT_PROVIDER = os.getenv('STT_PROVIDER', 'whisper')
TTS_PROVIDER = os.getenv('TTS_PROVIDER', 'eleven')
ADMIN_DASH_TOKEN = os.getenv('ADMIN_DASH_TOKEN', 'changeme_token')
OWNER_API_URL = os.getenv('OWNER_API_URL', '')
