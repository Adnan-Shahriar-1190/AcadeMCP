import os
import json

routine_path = os.path.join(os.path.dirname(__file__),"..","resources","aust_routine.json")
course_path = os.path.join(os.path.dirname(__file__),"..","resources","courses.json")

def load_routine()->dict:
    with open(routine_path,'r')as f:
        routine = json.load(f)
        return routine
    
def load_courses() -> dict:
    with open(course_path,'r')as f:
        courses = json.load(f)
        return courses
    
routine = load_routine()
courses = load_courses()