import os, json
from dotenv import load_dotenv
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from database.google_queries import load_token_from_db, save_token_to_db

load_dotenv()
#CREDENTIALS_FILE  = os.path.join(os.path.dirname(__file__),"..","credentials.json")
#TOKEN_FILE = os.path.join(os.path.dirname(__file__),"..","token.json")
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
        raise Exception("Google account not connected")

    creds = Credentials.from_authorized_user_info(
        token,
        SCOPES
    )

    if creds.expired:

        if not creds.refresh_token:
            raise Exception("Refresh token missing")

        creds.refresh(Request())

        await save_token_to_db(
            json.loads(creds.to_json())
        )

    return creds