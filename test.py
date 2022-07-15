import json

f = open ('data/blocks.json', "r")
  
# Reading from file
data = json.loads(f.read())

print(data)