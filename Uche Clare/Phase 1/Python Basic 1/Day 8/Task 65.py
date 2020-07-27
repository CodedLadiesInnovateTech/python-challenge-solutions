#program to convert seconds to day, hour, minutes and seconds.
def converter(secs):
  Minutes = round(secs/60, 3)
  Hour = round(secs/3600, 3)
  Day = round(secs/(3600*24), 3)
  return f" {secs} secs= {Minutes} minutes \n {secs} secs= {Hour} hours \n {secs} sec= {Day} days"
  
print(converter(6839299))

