#program to concatenate following dictionaries to create a new one.
print("new dict")
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for a in (dic1, dic2, dic3): dic4.update(a)
print(dic4)