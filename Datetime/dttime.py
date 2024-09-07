from datetime import date


todays_date = date.today() 

print("Today's date =", todays_date)

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))