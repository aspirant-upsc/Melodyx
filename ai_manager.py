import os
from config import AI_API_KEY

# Placeholder AI manager. Replace with your preferred LLM or API calls.

def ask_ai(prompt: str) -> str:
    if not AI_API_KEY:
        return 'AI not configured. Set AI_API_KEY in environment.'
    # Example: call a remote LLM provider
    return f'[AI response placeholder] {prompt[:200]}'
