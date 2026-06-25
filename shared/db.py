import os
import sqlite3

DB_path = os.path.join(os.path.dirname(__file__),"..","acadedb.db")
def init_db():
    with sqlite3.connect(DB_path) as c:
        c.execute(
            """
            create table if not exists quizes(
                id integer primary key autoincrement,
                date text not null,
                time text not null,
                course_name text not null,
                quiz_no int not null,
                course_no text,
                syllabus text not null,
                note text
            )
            """
        )