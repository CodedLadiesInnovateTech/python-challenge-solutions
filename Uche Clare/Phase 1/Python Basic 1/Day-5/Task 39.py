#program to compute the future value of a specified principal amount, rate of interest, and a number of years.
p_a=1000
r_o_i=3.5
n_o_y=7
s_i= int((p_a*r_o_i*n_o_y)/100)
print(s_i)
futurevalue=r_o_i+s_i
print(futurevalue)