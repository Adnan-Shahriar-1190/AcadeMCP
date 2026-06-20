from fastmcp import FastMCP
import os
import json
from datetime import datetime

routine_path = os.path.join(os.path.dirname(__file__),"resources","aust_routine.json")
DB_path = os.path.join(os.path.dirname(__file__),"acadeDB.db")

mcp = FastMCP(name='academcp')

def load_routine()->dict:
    with open(routine_path,'r')as f:
        routine = json.load(f)
        return routine
    
def get_class_start_time(time:str)->str:
    start_time = time.split('-')[0].strip()
    return start_time

routine = load_routine()

    
# routine tools
@mcp.tool
def get_current_datetime()->dict:
    """Get current date, time, and day."""

    now = datetime.now()
    return {
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "day": now.strftime("%A")
    }

@mcp.tool
def get_anyday_classes(day:str) ->dict:
    """
    Get all classes of a given day. Example: MONDAY, TUESDAY,WEDNESDAY.
    """
    day = day.upper().strip()
    #print(routine['schedule'])

    if day not in routine['schedule']:
        return {
            "success":False,
            "message":f"No classes for {day}."
        }
    
    classes = routine['schedule'][day]
    
    return{
        "success":True,
        "day":day,
        "classes": classes
    }

@mcp.tool
def get_today_all_classes()->dict:
    """
    Get Today's class based on current day
    """
    current = get_current_datetime()
    today = current["day"].upper()
    
    return get_anyday_classes(today)
    
@mcp.tool
def get_next_class_of_today()->dict:
    """
    Get the next class of the day based on current day and time.
    """
    current = get_current_datetime();
    current_day = current["day"]
    current_time = current['time']
    
    if current_day not in routine['schedule']:
        return {
            "success":False,
            "message":f"No classes for {current_day}."
        }
    
    classes = routine['schedule'][current_day]
    
    next_class=[]
    for cls in classes:
        start_time = get_class_start_time(cls['time'])
        print(start_time)
        if start_time > current_time[:5]:
            next_class.append(cls)
    
    if not next_class:
        return {
        "success": True,
        "has_next_class": False,
        "next_class": None,
        "message": "No more classes Today"
        
        }
        
    return {
    "success": True,
    "has_next_class": True,
    "next_class": next_class,
    "message": "Next class found."
    }


# exam tools
@mcp.tool
def add_exam():
    pass


#if __name__ == "__main__":
 #   mcp.run()
