from google_services import get_classroom_service

def list_courses() -> dict:
    """List all enrolled/teaching courses."""
    service = get_classroom_service()
    results = service.courses().list().execute()
    courses = results.get("courses", [])
    
    if not courses:
        return {"success": True, "courses": [], "message": "No courses found."}
    
    return {
        "success": True,
        "courses": [
            {
                "id": c["id"],
                "name": c["name"],
                "section": c.get("section", ""),
                "state": c.get("courseState", "")
            }
            for c in courses
        ]
    }

def get_course_announcements(course_id: str) -> dict:
    """Get announcements for a specific course."""
    service = get_classroom_service()
    results = service.courses().announcements().list(courseId=course_id).execute()
    announcements = results.get("announcements", [])
    
    return {
        "success": True,
        "announcements": [
            {
                "id": a["id"],
                "text": a.get("text", ""),
                "created": a.get("creationTime", "")
            }
            for a in announcements
        ]
    }

def get_course_assignments(course_id: str) -> dict:
    """Get all assignments (coursework) for a course."""
    service = get_classroom_service()
    results = service.courses().courseWork().list(courseId=course_id).execute()
    work = results.get("courseWork", [])
    
    return {
        "success": True,
        "assignments": [
            {
                "id": w["id"],
                "title": w.get("title", ""),
                "description": w.get("description", ""),
                "due": w.get("dueDate", "No due date"),
                "max_points": w.get("maxPoints", 0)
            }
            for w in work
        ]
    }