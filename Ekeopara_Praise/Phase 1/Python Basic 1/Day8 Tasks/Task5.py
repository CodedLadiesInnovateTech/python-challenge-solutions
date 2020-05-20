'''5. Write a Python program to convert seconds to day, hour, minutes and seconds.'''

def time_conv(sec):
    day = sec/(24*60*60)
    hour = sec/(60*60)
    minutes = sec/(60)
    return f"{sec} seconds:\n{day} days\n{hour} hours\n{minutes} minutes\n{sec} seconds"
print(time_conv(40000))
    