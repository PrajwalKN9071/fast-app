import requests
from app.core.config import settings

def generate_openai_text(prompt: str):
    headers = {
        "Content-Type": "application/json",
        "api-key": settings.AZURE_OPENAI_API_KEY
    }
    data = {
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1000
    }
    response = requests.post(
        f"{settings.AZURE_OPENAI_ENDPOINT}/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview",
        headers=headers,
        json=data
    )
    return response





