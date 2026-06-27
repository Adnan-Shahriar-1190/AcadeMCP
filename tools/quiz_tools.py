from database.quiz_queries import add_quiz_to_db,get_all_quizes_from_db,get_upcoming_quizzes_from_db,quizes_by_course_name_from_db

def register(mcp):
    @mcp.tool()
    async def add_quiz_exam(date:str, course_name:str, course_no:str, quiz_no:int, syllabus:str, time: str,room_no:str="", note:str="")->dict:
        """Add new quiz exam entry."""
        try:
            quiz_id = await add_quiz_to_db(date,course_name,course_no,quiz_no,syllabus,time,room_no,note)
            
            return {
            "success": True,
            "message": "Quiz added successfully!!",
            "quiz_id": quiz_id,
            }
        
        except Exception as e:
            return{
                "success":False,
                "message": str(e)
            }
            
    @mcp.tool()
    async def get_all_quizes()->dict:
        """Show all quizes in the database."""
        try:
            quizes = await get_all_quizes_from_db()
            
            return {
            "success": True,
            "message": f"{len(quizes)} quizes found.",
            "quizes": quizes,
            }
        
        except Exception as e:
            return{
                "success":False,
                "message": str(e)
            }
            
    @mcp.tool()
    async def get_upcoming_quizes()->dict:
        """Show all upcoming quizes in the database."""
        try:
            quizes = await get_upcoming_quizzes_from_db()
            
            return {
            "success": True,
            "message": f"{len(quizes)} upcoming quizes found.",
            "quizes": quizes,
            }
        
        except Exception as e:
            return{
                "success":False,
                "message": str(e)
            }
            
    @mcp.tool()
    async def get_courses_by_name(course_name:str)->dict:
        """Show the quizes in the db of a specific course name."""
        try:
            quizes = await quizes_by_course_name_from_db(course_name)
            
            return {
            "success": True,
            "message": f"{len(quizes)} quizes found.",
            "quizes": quizes,
            }
        
        except Exception as e:
            return{
                "success":False,
                "message": str(e)
            }
            
