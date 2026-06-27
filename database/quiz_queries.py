from shared.db import pool

async def add_quiz(
    date:str,
    course_name:str,
    course_no:str,
    quiz_no:int,
    syllabus:str,
    time: str|None = None,
    room_no:str="",
    note:str=""
):
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(
                """
                insert into quizes(date, course_name, course_no,quiz_no, syllabus, time, room_no, note)
                values (%s,%s,%s,%s,%s,%s,%s,%s) returning id;
                """,
                (date, course_name, course_no,quiz_no, syllabus, time,room_no, note),   
            )
            
            quiz_id = cur.fetchone()[0]
        await conn.commit()
        
    return quiz_id


async def get_all_quizes():
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute("""
                select date, course_name, quiz_no, syllabus FROM quizes
                order by date asc;
            """)

            quizes = await cur.fetchall()

    return quizes

async def get_upcoming_quizzes():
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(
                """
                select * from quizes
                where date > current_date or (date=current_date and time> current_time)
                order by date asc, time asc;
                """
            )
            quizzes = await cur.fetchall()
    return quizzes

async def get_quizzes_by_course_name(course_name: str):
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(
                """
                SELECT *
                FROM quizes
                WHERE course_name ILIKE %s
                ORDER BY date ASC, time ASC;
                """,
                (f"%{course_name}%",),
            )

            quizzes = await cur.fetchall()

    return quizzes
