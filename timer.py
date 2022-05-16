#beleow is code that is used to generate timer to be used
# the requirements needed is the importation of time module,and creating a function that will create a countdown timer and while loop
import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
    username=input("username is ")
    print("stop Execusion done by" + " " + username )

countdown(6)