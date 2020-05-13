from datetime import date


def diff_in_date(first, second):
    value = str(second - first)
    if value.__contains__(','):
        generated_sum = value.split(',')
        return generated_sum[0]
    else:
        return value


first_date = date(2014, 7, 2)
second_date = date(2014, 7, 11)
current_date = date.today()

val = diff_in_date(first_date, second_date)
print(val)

newVal = diff_in_date(second_date, current_date)
print(newVal)
