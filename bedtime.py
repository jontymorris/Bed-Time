import datetime, sched, time, os

# Commands the OS to shutdown
def shutdown():
    os.system("shutdown -s")

# Return's whether it's time for bed
def is_bedtime(time):
    # Check for Friday or Saturday
    if time.weekday() in [4, 5]:
        # Is it past 11 pm and before 4 am
        if time.hour >= 23 or time.hour <= 4:
            return True
    
    else:
        # Is it past 9:30 pm and before 4 am
        if time.hour > 21 or (time.hour == 21 and time.minute >= 30) or time.hour <= 4:
            return True
    
    # It is not bedtime
    return False

def main():
    now = datetime.datetime.now()

    # If it's bedtime then shutdown
    if is_bedtime(now):
        shutdown()

# Is it running the unit tests?
if __name__ == "__main__":
    timer = sched.scheduler(time.time, time.sleep)
    timer.enter(5, 1, main)
    
    # Run every five minutes
    while True:
        timer.enter(60*5, 1, main)
        timer.run()