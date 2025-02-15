# Today I make countdown project

import time
def countdown(seconds):
    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print(time_format, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")


# User input
total_seconds = int(input("Enter the time in seconds: "))
if total_seconds < 0:
    print("Please enter a positive number")
else:
    countdown(total_seconds)
