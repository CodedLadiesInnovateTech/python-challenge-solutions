#convert all units of time into seconds.
def units_time(minutes, hour, day, week, yr):
  Mins = minutes * (60)
  Hours = hour * (60*60)
  Days = day *(60*60*24)
  Weeks = week * (60*60*24*7)
  Years = yr * (60*60*24*7*52)
  return f" {minutes} minutes= {Mins} secs \n {hour} Hours= {Hours} secs \n {day} Days= {Days} secs \n {week} Weeks= {Weeks} secs \n {yr} Years= {Years} secs"

print(units_time(3, 3, 5, 6, 4))
