import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/classroom.courses.readonly"]

creds = None

# 1. Load saved login session
if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)

# 2. If not valid → login once
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json",
            SCOPES
        )
        creds = flow.run_local_server(port=8080)

    # 3. Save session (THIS IS THE KEY)
    with open("token.json", "w") as token:
        token.write(creds.to_json())

# 4. Use API
service = build("classroom", "v1", credentials=creds)

courses = service.courses().list().execute()
print(courses)