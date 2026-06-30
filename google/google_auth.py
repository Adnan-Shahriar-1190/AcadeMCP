import os, json
from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from database.google_queries import load_token_from_db, save_token_to_db
from google.auth.exceptions import RefreshError

load_dotenv()
GOOGLE_CREDENTIALS = json.loads(os.environ["GOOGLE_CREDENTIALS"])

SCOPES = [
    "https://www.googleapis.com/auth/classroom.courses.readonly",
    "https://www.googleapis.com/auth/classroom.announcements.readonly",
    "https://www.googleapis.com/auth/classroom.courseworkmaterials.readonly",
    "https://www.googleapis.com/auth/classroom.student-submissions.me.readonly"
]

async def get_credentials():
    token = await load_token_from_db()
    if token is None:
        raise Exception("Google account not connected!!")
    creds = Credentials.from_authorized_user_info(
        token,
        SCOPES
    )
    if creds.expired or not creds.valid:
        if not creds.refresh_token:
            raise Exception(
                "Refresh token missing"
            )
        
        try:
            creds.refresh(Request())
            
        except RefreshError:
            raise Exception(
                "Refresh Token is Invalid. Need to run (google_login.py) locally."
            )

        await save_token_to_db(
            json.loads(creds.to_json())
        )

    return creds