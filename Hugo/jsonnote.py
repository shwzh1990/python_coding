import json
info = ["12345,Jack,chinese:100,Math:100,English:100"]

info2 = {"12345":{'Jack':{"chinese":'100'}}}

result = json.dumps(info2, indent = 4)

with open("1.txt",'w') as fd:
    fd.write(result)


with open("1.txt",'r') as fd:
    info = fd.read()
result = json.loads(info)

