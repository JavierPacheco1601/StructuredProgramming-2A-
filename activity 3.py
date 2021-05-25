price_hour = 300
hours = int(input("How many hours did you work?\n"))
min_hours = 12
hours_extra = hours*min_hours
bon = 2


if(hours >= 40):
    hours_extra = hours*min_hours
    salary = (min_hours*price_hour) + (hours_extra*(price_hour*bon))

else:
    salary = hours*price_hour

print("You will be payed ",salary)