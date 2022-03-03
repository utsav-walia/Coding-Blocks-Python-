import json

with open("data.json","r") as file:
    d = json.load(file)
    print(d["name"])

# Dictionary to json

a = {'name':'utsav', 'mark','90'}
with open("data2.json","r") as file:
    json.dump(a,file)
