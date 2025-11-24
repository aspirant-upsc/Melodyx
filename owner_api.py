import requests
from config import OWNER_API_URL

def fetch_owner_info():
    if not OWNER_API_URL:
        return {'error': 'OWNER_API_URL not set'}
    try:
        r = requests.get(OWNER_API_URL, timeout=6)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {'error': str(e)}
