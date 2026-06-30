from shared.config import courses
from google.google_services import get_classroom_service
from google.oauth import create_flow

def register(mcp):

    @mcp.tool()
    def all_course_details() ->dict:
        """
        List all active courses with their formal names, course_id, and aliases.
        Call this first to resolve a user's shorthand (e.g. 'DA', 'image processing')
        to the correct course name or ID before passing to other tools.
        """
        return {
            "success":True,
            "message":"Courses Retrived successfully.",
            "courses" : courses
        }

    @mcp.tool()
    async def get_course_announcements(course_id: str) -> dict:
        """Get announcements for a specific course."""
        try:
            service = await get_classroom_service()

            results = (
                service.courses().announcements().list(courseId=course_id,pageSize=3).execute()
            )

            announcements = results.get("announcements", [])

            return {
                "success": True,
                "count": len(announcements),
                "announcements": [
                    {
                        "id": a["id"],
                        "text": a.get("text", ""),
                        "created": a.get("creationTime", ""),
                        "updated": a.get("updateTime", ""),
                    }
                    for a in announcements
                ]
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    @mcp.tool()
    async def get_course_assignements(course_id:str)->dict:
        """Get assignments for a specific course."""
        try:
            service = await get_classroom_service()
            results = (
                service.courses().courseWork().list(courseId=course_id,pageSize=3).execute()
            )
            assignments = results.get("courseWork", [])
            return {
                "success": True,
                "count": len(assignments),
                "assignments": [
                    {
                        "id": a["id"],
                        "title": a.get("text", ""),
                        "description": a.get("description", ""),
                        "work_type": a.get("workType", ""),
                        "created": a.get("creationTime", ""),
                        "updated": a.get("updateTime", ""),
                        "due_date": a.get("dueDate")
                    }
                    for a in assignments
                ]
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    @mcp.tool()
    async def get_course_materials(course_id:str)->dict:
        """Get course materials for a specific course."""
        try:
            service = await get_classroom_service()
            results = (
                service.courses().courseWorkMaterials().list(courseId=course_id).execute()
            )
            materials = results.get("courseWorkMaterial", [])
            return {
                "success": True,
                "count": len(materials),
                "materials": [
                    {
                        "id": m["id"],
                        "title": m.get("text", ""),
                        "description": m.get("description", ""),
                        "created": m.get("creationTime", ""),
                        "updated": m.get("updateTime", ""),
                        "materials": m.get("materials",[])
                    }
                    for m in materials
                ]
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
