from shared.config import routine
from datetime import datetime


def get_class_start_time(time:str)->str:
    start_time = time.split('-')[0].strip()
    return start_time


def register(mcp): 
    
    @mcp.tool()
    def get_current_datetime()->dict:
        """Get current date, time, and day."""

        now = datetime.now()
        return {
            "success": True,
            "date": now.strftime("%Y-%m-%d"),
            "time": now.strftime("%H:%M:%S"),
            "day": now.strftime("%A")
        }

    @mcp.tool()
    def get_anyday_classes(day:str) ->dict:
        """
        Get all classes of a given day. Example: MONDAY, TUESDAY,WEDNESDAY.
        """
        day = day.upper().strip()
        
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

    @mcp.tool()
    def get_today_all_classes()->dict:
        """
        Get Today's class based on current date and time.
        """
        current = get_current_datetime()
        today = current["day"].upper()
        
        return get_anyday_classes(today)
        
    @mcp.tool
    def get_next_class_of_today()->dict:
        """
        Get the next class of today.
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

