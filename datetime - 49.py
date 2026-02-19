from datetime import date, time , datetime
today = date.today()
now = datetime.now()
print("Today is \n", today)
print("The time right now is \n", now)
print("\n Date components: ", today.year, today.month, today.day)