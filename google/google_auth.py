import os, json
from dotenv import load_dotenv
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

load_dotenv()
#CREDENTIALS_FILE  = os.path.join(os.path.dirname(__file__),"..","credentials.json")
TOKEN_FILE = os.path.join(os.path.dirname(__file__),"..","token.json")
GOOGLE_CREDENTIALS = json.loads(os.environ["GOOGLE_CREDENTIALS"])

SCOPES = [
    "https://www.googleapis.com/auth/classroom.courses.readonly",
    "https://www.googleapis.com/auth/classroom.announcements.readonly",
    "https://www.googleapis.com/auth/classroom.courseworkmaterials.readonly",
    "https://www.googleapis.com/auth/classroom.student-submissions.me.readonly"
]

def get_credentials():
    creds = None
    # Load saved login session
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    # If not valid,login again
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_config(
                GOOGLE_CREDENTIALS,
                SCOPES
            )
            creds = flow.run_local_server(port=8080)

        # save session token
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())
    return creds

print(GOOGLE_CREDENTIALS)