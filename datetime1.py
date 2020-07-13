import datetime

today = datetime.datetime.now()
print("today = ",today)
midnight = today.replace(hour=0,minute=0,second=0,microsecond=0)
print("midnight = ",midnight)
day = today.day
yes = day - 1
yes_mid = midnight.replace(day=yes)
print("day = ",day)
print("----------")
print(midnight.strftime("%d-%b-%Y %H:%M:%S"))
print(yes_mid.strftime("%d-%b-%Y %H:%M:%S"))

