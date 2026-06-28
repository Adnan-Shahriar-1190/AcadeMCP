from googleapiclient.discovery import build
from google.google_auth import get_credentials

async def get_classroom_service():
    from googleapiclient.discovery import build
    creds = await get_credentials()
    return build("classroom", "v1", credentials=creds,cache_discovery=False)
