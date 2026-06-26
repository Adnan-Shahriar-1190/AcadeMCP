from database.quiz_queries import add_quiz

def register(mcp):
    @mcp.tool()
    def add_quiz_exam(date:str, course_name:str, course_no:str, quiz_no:int, syllabus:str, time: str,room_no:str="", note:str="")->dict:
        """Add new quiz exam entry."""
        try:
            quiz_id = add_quiz(date,course_name,course_no,quiz_no,syllabus,time,room_no,note)
            
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
    def get_all_quizes()->dict:
        """Show all quizes in the database."""
        try:
            quizes = get_all_quizes()
            
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
    def get_upcoming_quizes()->dict:
        """Show all upcoming quizes in the database."""
        try:
            quizes = get_upcoming_quizes()
            
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
            
