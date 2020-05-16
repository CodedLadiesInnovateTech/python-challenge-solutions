#differences in date of the day

import datetime
#import timedelta
from datetime import date

first = date(2014, 7, 2)
second = date(2014, 7, 11)
diff = second - first
print(diff.days)