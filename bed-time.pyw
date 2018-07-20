import datetime, sched, time, os

def shutdown():
    os.system("shutdown -s")

def main():
    now = datetime.datetime.now()

    # Check for Friday or Saturday
    if now.weekday() in [4, 5]:
        # Is it past 11 pm and before 4 am
        if now.hour >= 23 or now.hour <= 5:
            shutdown()
    
    else:
        # Is it past 9:30 pm and before 4 am
        if (now.hour > 21 or (now.hour == 21 and now.minute >= 30)) and now.hour <= 5:
            shutdown()

if __name__ == "__main__":
    timer = sched.scheduler(time.time, time.sleep)
    timer.enter(5, 1, main)
    
    # Run every five minutes
    while True:
        timer.enter(60*5, 1, main)
        timer.run()