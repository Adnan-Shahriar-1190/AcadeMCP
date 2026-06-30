from shared.db import pool

async def init_db():
    async with pool.connection() as conn:
            await conn.execute("""
                create table if not exists quizes(
                    id serial primary key,
                    date date not null,
                    time Time,
                    course_name varchar(40) not null,
                    course_no varchar(30) not null,
                    room_no varchar(30),
                    quiz_no integer not null,
                    syllabus varchar(200) not null,
                    note varchar(100)
                ); 
            """)
            
            await conn.execute("""
                create table if not exists google_tokens (
                    id serial primary key,
                    token JSONB not null
                );
            """)
            
            await conn.execute(
                """
                create table if not exists absences(
                    id serial primary key,
                    date date not null,
                    course_no varchar(30) not null,
                    course_name varchar(30) not null,
                    time Time not null
                );
            """)
            
