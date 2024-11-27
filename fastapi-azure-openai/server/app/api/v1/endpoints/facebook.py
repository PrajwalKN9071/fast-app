from fastapi import APIRouter, HTTPException, Query
from app.services.facebook_service import get_facebook_login_url, get_access_token, fetch_user_data

router = APIRouter()

@router.get("/login")
async def login():
    """
    Endpoint to redirect users to Facebook login.
    """
    login_url = get_facebook_login_url()
    return {"login_url": login_url}

@router.get("/callback")
async def callback(code: str = Query(...)):
    """
    Handle Facebook OAuth callback and fetch user data.
    """
    try:
        access_token = get_access_token(code)
        user_data = fetch_user_data(access_token)
        return {"user_data": user_data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
