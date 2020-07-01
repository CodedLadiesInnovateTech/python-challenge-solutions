#program to create a new JSON file from an existing JSON file.
import json

with open('states.json') as f:
  state_data= json.load(f)

for state in state_data['states']:
  del state['area_codes']

with open('new_states.json', 'w') as f:
  json.dump(state_data, f, indent=2)