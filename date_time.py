
from datetime import datetime

if __name__ == "__main__":
    try:
        today_day = datetime.now()
        print("Today's Date is : ", today_day)
        start_time = datetime.now()
        print("Today's Date and Time is : ", start_time)
        end_time = datetime.now()
        print("Today's Date and Time is : ", end_time)

        elapse_time = start_time - end_time
        print(elapse_time)
    except:
        print("invalid date")

