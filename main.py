from fastmcp import FastMCP
import math
import json
from datetime import datetime

mcp = FastMCP(name='academcp')

def load_routine()->dict:
    with open('resources/aust_routine.json','r')as f:
        routine = json.load(f)
        return routine
        
routine = load_routine()
    
# routine tools

@mcp.tool
def get_current_datetime():
    """Get current date, time, and day."""

    now = datetime.now()
    return {
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "day": now.strftime("%A")
    }

@mcp.tool
def get_anyday_classes(day:str) ->str:
    """
    Get all classes of a given day. Example: MONDAY, TUESDAY,WEDNESDAY.
    """
    day = day.upper().strip()

    if day not in routine['schedule']:
        return f"Invalid day. No classes on {day}."
    
    classes = routine['schedule'][day]
    
    #print(classes)
    
    result = f"Classes on {day}: \n\n"
    for cls in classes:
        result += (
            f"Course: {cls['course']} \n"
            f"Time : {cls['time']} \n"
            f"Room : {cls['room']} \n"
            f"Teacher : {cls['teacher']} \n"
            f"Type : {cls['type']} \n"
        )
    return result

@mcp.tool
def get_today_classes(day:str='',date:str='')->str:
    """
    Get Today's class based on current day
    """
    current = get_current_datetime()
    today = current["day"].upper()
    
    return get_anyday_classes(today)
    

@mcp.tool
def get_next_class():
    """
    Get the next class of the day based on current day and time.
    """
    current = get_current_datetime();
    today = current["day"]
    time = current['time']
    
    

@mcp.tool
def get_course_info():
    pass

@mcp.tool
def put_exam_day_and_time():
    pass


@mcp.tool
def add_apples(num1:int,num2:int)->int:
    return (math.pow(num1,2) + num2)

#if __name__ == "__main__":
 #   mcp.run()
