import sqlite3
from shared.db import DB_path

def register(mcp):
    @mcp.tool()
    def add_quiz_exam(date:str, time:str, course_name:str,quiz_no:int,syllabus:str, course_no:str="", note:str="")->dict:
        """Add new quiz exam entry with Date, Time , course Name, Quiz_no and syllabus"""
        with sqlite3.connect(DB_path) as c:
            cur = c.execute(
                "insert into quizes(date,time,course_name,quiz_no,syllabus,course_no,note) values(?,?,?,?,?,?,?)",
                (date,time,course_name,quiz_no,syllabus,course_no,note)
            )
            return{
                "success": True,
                "message": "Quiz inserted successfully!",
                "id":cur.lastrowid
            }