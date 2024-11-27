import requests
from urllib.parse import urlencode
from app.core.config import settings

def get_facebook_login_url():
    """
    Generate the Facebook login URL for user authentication.
    """
    params = {
        "client_id": settings.FB_APP_ID,
        "redirect_uri": settings.FB_REDIRECT_URI,
        "scope": "user_likes,user_events",
        "response_type": "code",
    }
    return f"https://www.facebook.com/v12.0/dialog/oauth?{urlencode(params)}"

def get_access_token(auth_code: str):
    """
    Exchange the authorization code for an access token.
    """
    url = "https://graph.facebook.com/v12.0/oauth/access_token"
    params = {
        "client_id": settings.FB_APP_ID,
        "redirect_uri": settings.FB_REDIRECT_URI,
        "client_secret": settings.FB_APP_SECRET,
        "code": auth_code,
    }
    response = requests.get(url, params=params)
    response_data = response.json()
    
    if response.status_code != 200 or "access_token" not in response_data:
        raise Exception(f"Error retrieving access token: {response_data}")
    
    return response_data["access_token"]

def fetch_user_data(access_token: str):
    """
    Fetch user data from Facebook Graph API.
    """
    url = "https://graph.facebook.com/v12.0/me"
    params = {
        "fields": "id,name,likes{name},events",
        "access_token": access_token,
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Error fetching user data: {response.json()}")
    return response.json()
