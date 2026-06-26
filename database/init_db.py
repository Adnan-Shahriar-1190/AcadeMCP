from shared.db import pool

def init_db():
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                create table if not exists quizes(
                    id serial primary key,
                    date date not null,
                    time Time,
                    course_name varchar(40) not null,
                    course_no varchar(10) not null,
                    room_no varchar(10),
                    quiz_no integer not null,
                    syllabus varchar(200) not null,
                    note varchar(100)
                );    
            """)
            
        conn.commit()