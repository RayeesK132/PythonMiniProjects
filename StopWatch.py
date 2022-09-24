from signal import pause
import time

#My first attempt
hour = 00
min = 00
sec = 00

print('Type ENTER to start & CTRL-C to stop.')
start = input('')

while True:
    if start == '' :
        sec = sec + 1
        if sec == 60:
            min = min + 1
            sec = 00
        if min == 60:
            hour = hour + 1
            min = 00
        time.sleep(1)
        print(hour, ':', min, ':', sec)