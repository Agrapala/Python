import datetime
b_day = datetime.date(2002,1,30)
print(b_day)

today = datetime.date.today()
print(today)

age = today - b_day
print(age)