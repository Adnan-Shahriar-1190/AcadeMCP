from googleapiclient.discovery import build
from google_auth import get_credentials
import json, os

def get_classroom_service():
    from googleapiclient.discovery import build
    creds = get_credentials()
    return build("classroom", "v1", credentials=creds)

def get_drive_service():
    creds = get_credentials()
    return build("drive", "v3", credentials=creds)

'''
client = get_classroom_service()
results = client.courses().list().execute()
results = results['courses']

courses_data = []

for i, cls in enumerate(results):
    if cls['courseState'] == 'ACTIVE':
        courses_data.append({
            "google_classroom_id": cls['id'],
            "name": cls['name'],
            "section": cls.get('section', ''),
            "calendarId": cls.get('calendarId', ''),
            "courseState" : cls['courseState'],
            "aliases": []
        })

# Save to JSON
output_path = os.path.join(os.path.dirname(__file__), "resources", "courses.json")
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, 'w') as f:
    json.dump({"courses": courses_data}, f, indent=4)

print(f"Saved {len(courses_data)} active courses to courses.json")
'''