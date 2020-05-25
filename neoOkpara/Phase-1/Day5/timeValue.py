def calc_prt(p, r, t):
    r = r / 100
    final_amount = p * (1 + (r * t))
    return final_amount


get_value = calc_prt(10000, 3.5, 7)
print (round(get_value, 2))
