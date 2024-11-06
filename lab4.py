
from datetime import datetime


def is_authorized():
    return True

def day_only(func):
    def wrapper():
        current_hour = datetime.now().hour
        if current_hour <= 6 and current_hour >= 18:
            return "it is not day"
        if not is_authorized(): 
            return "you are not authorized"
        return func()
    return wrapper 

@day_only
def Do_A():
    return "Do A"
@day_only
def Do_B():
    return "Do B"

@day_only
def Do_C():
    return "Do C"


print(Do_A())
print(Do_B())
print(Do_C())

