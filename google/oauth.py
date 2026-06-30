from google_auth_oauthlib.flow import Flow
import os, json

GOOGLE_CREDENTIALS = json.loads(
    os.environ["GOOGLE_CREDENTIALS"]
)

SCOPES = [
    "https://www.googleapis.com/auth/classroom.courses.readonly",
    "https://www.googleapis.com/auth/classroom.announcements.readonly",
    "https://www.googleapis.com/auth/classroom.courseworkmaterials.readonly",
    "https://www.googleapis.com/auth/classroom.student-submissions.me.readonly",
]

REDIRECT_URI ="https://helixion.fastmcp.app/auth/callback"


def create_flow():

    flow = Flow.from_client_config(
        GOOGLE_CREDENTIALS,
        scopes=SCOPES
    )

    flow.redirect_uri = REDIRECT_URI

    return flow