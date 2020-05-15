import calendar


def calendarKnow(yearNo, monthNo): 
    print(calendar.month(yearNo, monthNo))


year = int(input("Input the yearNo : "))
month = int(input("Input the monthNo : "))

calendarKnow(year, month)
