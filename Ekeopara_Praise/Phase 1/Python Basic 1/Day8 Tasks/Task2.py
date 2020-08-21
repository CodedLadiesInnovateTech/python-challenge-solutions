
'''2. Write a Python program to convert all units of time into seconds.'''
def time_conv(ty, tmo, twk, tdy, thr, tmin):

    yr = 365 * 24 * 60 * 60 * ty
    mont = 30 * 24 * 60 * 60 *tmo
    week = 7 * 24 * 60 * 60 * twk
    days =  24  * 60 * 60 * tdy
    hrs= 60*60 * thr
    mins =60* tmin
    return f"{ty} year ={yr} seconds\n{tmo} month = {mont} seconds\n{twk} week  = {week} seconds\n{tdy}day = {days} seconds\n{thr} hour = {hrs} seconds\n{tmin} minute = {mins} seconds"

print(time_conv(1, 1, 1, 1, 1, 1))
