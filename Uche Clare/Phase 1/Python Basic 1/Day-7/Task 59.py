def to_centimeters(f, i):
 x = (f * 30.48) 
 y = (i * 2.54)
 return x, y

print(to_centimeters(7, 8))
   