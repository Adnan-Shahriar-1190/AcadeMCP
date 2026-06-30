from shared.db import pool

async def insert_absent_to_db(date:str,course_no:str,course_name:str):
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(
                """
                insert into absences (date, course_no, course_name)
                values (%s, %s, %s) returning id;
                """,
                (date,course_no, course_name),   
            )
            
            row = await cur.fetchone()
            absent_id = row[0]
        await conn.commit()
    return absent_id

async def get_absences_by_course_from_db(course_name:str):
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(
                """
                select date, course_no, course_name from absences
                where lower(course_name) = lower(%s)
                ORDER BY date DESC;
                """,(course_name,)
            )
            absents = await cur.fetchall()
    return absents

async def get_absence_count_by_course_from_db(course_name: str):
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(
                """
                select count(*) as absent_count from absences
                where lower(course_name) = lower(%s));
                """,
                (course_name,),
            )
            row = await cur.fetchone()

    return row[0] if row else 0

async def get_absence_count_all_courses_from_db():
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

async def delete_absent_from_db(date:str, course_name:str):
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(
                """
                delete from absences
                where date = %s and lower(course_name)=lower(%s) returning id;
                """, (date,course_name),
            )
            row = await cur.fetchone()
        await conn.commit()
    return row[0] if row else None