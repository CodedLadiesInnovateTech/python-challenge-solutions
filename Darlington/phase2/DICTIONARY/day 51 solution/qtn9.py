#program to store a given dictionary in a json file.
d = {"students":[{"firstName": "Nikki", "lastName": "Roysden"},
               {"firstName": "Mervin", "lastName": "Friedland"},
               {"firstName": "Aron ", "lastName": "Wilkins"}],
"teachers":[{"firstName": "Amberly", "lastName": "Calico"},
         {"firstName": "Regine", "lastName": "Agtarap"}]}
print("Original dictionary:")
print(d)
print(type(d))
import json
 
with open("dictionary", "w") as f:
   json.dump(d, f, indent = 4, sort_keys = True)
 
print("\nJson file to dictionary:")
with open('dictionary') as f:
 data = json.load(f)
print(data)