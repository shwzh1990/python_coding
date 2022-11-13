import json
with open("student_sample.txt",'r') as fd:
    data = json.load(fd)
#student_structure = json.loads(data)
#print(student_structure)
#print(student_structure["1234"])
data["1234"]["Chinese"] = 69

#student_data = json.dumps(data)
#with open("student_sample.txt",'w') as fd:
#    fd.write(student_data)

with open("student_sample.txt",'w') as fd:
    json.dump(data, fd)