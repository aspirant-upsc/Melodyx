import os
from config import STT_PROVIDER, TTS_PROVIDER

# STT/TTS abstraction layer. Replace with real provider integration.

def transcribe(path: str) -> str:
    # stub: read file and pretend
    return 'transcribed text from ' + path

def synthesize(text: str, out_path: str) -> str:
    # stub: create empty file as placeholder
    with open(out_path, 'wb') as f:
        f.write(b'')
    return out_path
