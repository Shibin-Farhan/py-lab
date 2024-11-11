import time
from datetime import datetime

current_datetime = datetime.now()


print("Current date and time:", current_datetime)


print("Current year:", current_datetime.year)


print("Month of the year:", current_datetime.strftime("%B"))


print("Week number of the year:", current_datetime.strftime("%U"))


print("Weekday of the week:", current_datetime.strftime("%A"))


print("Day of the year:", current_datetime.strftime("%j"))


print("Day of the month:", current_datetime.day)


print("Day of the week (0=Monday, 6=Sunday):", current_datetime.weekday())

