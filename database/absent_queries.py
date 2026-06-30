from shared.db import pool

async def insert_absent(date:str,course_no:str,course_name:str):
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(
                """
                insert into absences (date, course_no, course_name)
                values ($1, $2, $3) returning id;
                """,
                (date,course_no, course_name),   
            )
            
            row = await cur.fetchone()
            absent_id = row[0]
        await conn.commit()
    return absent_id

async def get_absences_by_course(course_name:str):
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(
                """
                select date, course_no, course_name from absences
                where lower(course_name) = lower($1)
                ORDER BY date DESC;
                """,(course_name,)
            )
            absents = await cur.fetchall()
    return absents

async def get_absence_count_by_course(course_name: str):
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(
                """
                select count(*) as absent_count from absences
                where lower(course_name) = lower($1);
                """,
                (course_name,),
            )
            row = await cur.fetchone()

    return row[0] if row else 0

async def get_absence_count_all_courses():
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(
                """
                select course_name, course_no, count(*) as absent_count
                from absences
                group by course_name, course_no
                order by absent_count desc;
                """
            )
            return await cur.fetchall()
