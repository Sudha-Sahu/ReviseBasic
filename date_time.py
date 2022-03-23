from datetime import datetime
import time


if __name__ == "__main__":
    today_day = datetime.now()
    print("Today's Date is : ", today_day)
    start_time = time.time()
    print("Start Time is : ", start_time)
    time.sleep(5)
    end_time = time.time()
    print("End Time is : ", end_time)

    elapse_time = end_time - start_time
    print(f"Time Elapsed(seconds) --> {elapse_time}")
