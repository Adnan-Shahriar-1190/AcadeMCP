from shared.db import pool

def add_quiz(
    date:str,
    course_name:str,
    course_no:str,
    quiz_no:int,
    syllabus:str,
    time: str|None = None,
    room_no:str="",
    note:str=""
):
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                insert into quizes(date, course_name, course_no,quiz_no, syllabus, time, room_no, note)
                values (%s,%s,%s,%s,%s,%s,%s,%s) returning id;
                """,
                (date, course_name, course_no,quiz_no, syllabus, time,room_no, note),   
            )
            
            quiz_id = cur.fetchone()[0]
        conn.commit()
        
    return quiz_id


def get_all_quizzes():
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                select date, course_name, quiz_no, syllabus, FROM quizes
                order by date asc;
            """)

            quizes = cur.fetchall()

    return quizes

def get_upcoming_quizzes():
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                select * from quizes
                where date > current_date or (date=current_date and time> current_time)
                order by date asc, time asc;
                """
            )
            quizzes = cur.fetchall()
    return quizzes

def get_quizzes_by_course_name(course_name: str):
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT *
                FROM quizes
                WHERE course_name ILIKE %s
                ORDER BY date ASC, time ASC;
                """,
                (f"%{course_name}%",),
            )

            quizzes = cur.fetchall()

    return quizzes
