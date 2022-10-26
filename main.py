from datetime import datetime
from playsound import playsound

def validate_time(alarm_time):
    if len(alarm_time) != 11:
        return 'Invalid time format! Try again..'
    else:
        if int(alarm_time[0:2]) > 12:
            return 'Invalid HOUR format! Try again..'
        elif int(alarm_time[3:5]) > 59:
            return 'Invalid MINUTE format! Try again..'
        elif int(alarm_time[6:8]) > 59:
            return 'Invalid SECOND format! Try again..'
        else:
            return "ok"

while True:
    alarm_time = input('Please input alarm time in format: HH:MM:SS AM/PM :')
    validate = validate_time(alarm_time.lower())
    if validate != "ok":
        print(validate)
    else:
        print(f'Setting alarm to: {alarm_time}')
        break

alarm_hour = alarm_time[0:2]
alarm_minutes = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:].upper()

while True:
    now = datetime.now()
    currenthour = now.strftime("%I")
    currentminutes = now.strftime("%M")
    currentseconds = now.strftime("%S")
    current_period = now.strftime("%p")

    if alarm_period == current_period:
        if alarm_hour == currenthour:
            if alarm_minutes == currentminutes:
                if alarm_seconds == currentseconds:
                    print('Wake up!!!!!')
                    playsound('./sound.mp3')
                    break

