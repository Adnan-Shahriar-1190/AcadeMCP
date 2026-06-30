from database.absent_queries import insert_absent_to_db, get_absences_by_course_from_db, get_absence_count_by_course_from_db, get_absence_count_all_courses_from_db,delete_absent_from_db


def register(mcp):

    @mcp.tool()
    async def add_absent(date: str, course_no: str, course_name: str) -> dict:
        """
        Record a new absence entry in the database.

        Use this tool when the user wants to log that they were absent from a class.
        Resolve the course name and course number from the user's course list before calling.

        Args:
            date:        Date of absence in YYYY-MM-DD format.
            course_no:   Course code/number (e.g. "CSE-4209").
            course_name: Full course name (e.g. "Data Analysis" or "Computer Graphics").
        """
        try:
            absent_id = await insert_absent_to_db(date, course_no, course_name)

            return {
                "success": True,
                "message": "Absence recorded successfully!!",
                "absent_id": absent_id,
            }

        except Exception as e:
            return {
                "success": False,
                "message": str(e)
            }

    @mcp.tool()
    async def get_absences_for_course(course_name: str) -> dict:
        """
        Retrieve all recorded absences for a specific course.

        Args:
            course_name: Full course name (e.g. "Data Analysis" or "Computer Graphics").
        """
        try:
            absences = await get_absences_by_course_from_db(course_name)

            return {
                "success": True,
                "message": f"{len(absences)} absences found.",
                "absences": absences,
            }

        except Exception as e:
            return {
                "success": False,
                "message": str(e)
            }

    @mcp.tool()
    async def get_absence_count_for_course(course_name: str) -> dict:
        """
        Get the total number of absences for a specific course.

        Args:
            course_name: Full course name (e.g. "Data Analysis" or "Computer Graphics").
        """
        try:
            count = await get_absence_count_by_course_from_db(course_name)

            return {
                "success": True,
                "message": f"{count} absences found for {course_name}.",
                "absent_count": count,
            }

        except Exception as e:
            return {
                "success": False,
                "message": str(e)
            }

    @mcp.tool()
    async def get_absence_summary() -> dict:
        """
        Get absence counts grouped by course, sorted from most to least absences.
        Use this when the user wants an overview of absences across all courses.
        """
        try:
            summary = await get_absence_count_all_courses_from_db()

            return {
                "success": True,
                "message": f"Absence summary for {len(summary)} courses.",
                "summary": summary,
            }

        except Exception as e:
            return {
                "success": False,
                "message": str(e)
            }
    
    @mcp.tool()
    async def delete_absent(absent_id: int) -> dict:
        """
        Delete an absence entry by its ID.Use this when the user wants to remove a previously recorded absence.
        Args:
            absent_id: The ID of the absence record to delete.
        """
        try:
            deleted_id = await delete_absent_from_db(absent_id)

            if deleted_id is None:
                return {
                    "success": False,
                    "message": f"No absence found with id {absent_id}.",
                }

            return {
                "success": True,
                "message": "Absence deleted successfully!!",
                "absent_id": deleted_id,
            }

        except Exception as e:
            return {
                "success": False,
                "message": str(e)
            }