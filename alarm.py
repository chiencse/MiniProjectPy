from datetime import datetime

alarm_time = input('Alarm Time weakup (HH:MM:SS): ')
alarm_h, alarm_m, alarm_s = alarm_time.split(":")
print(alarm_h, alarm_m, alarm_s)
while True:
    today = datetime.now()
    # print(today)
    cur_h = today.strftime("%I")
    cur_m = today.strftime("%M")
    cur_s = today.strftime("%S")
    print(cur_h, cur_m, cur_s)
    if alarm_h == cur_h:
        if alarm_m == cur_m:
            if alarm_s == cur_s:
                print("Alarm !")
                break


