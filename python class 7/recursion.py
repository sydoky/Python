'''def factorial(number):
    if number == 100:
        return 100
    return number + factorial(number +1)

print(factorial(99))'''

'''def function(num1, num2):
    print(num1, num2)
    if num2 == 0:
        return num1
    return function(num1/10, num2 - 1)

print(function(1000000, 3))


def function(1000000, 3):
    print(1000000, 3)
    if 3 == 0:
        return 1000000
    return function(100000, 2)

print(function(1000000, 3))


def function(1000000, 3):
    print(1000000, 3)
    return 1000'''


import pytz
import datetime

country='Europe/Moscow'

tz_to_display=pytz.timezone(country)
local_time=datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country,local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))








