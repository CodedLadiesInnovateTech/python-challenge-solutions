
# dates: (2014, 7, 2), (2014, 7, 11)


from datetime import date

firstDate = date(2013, 7, 12)
secondDate = date(2014, 7, 11)
diff = secondDate - firstDate
print(diff.days)
