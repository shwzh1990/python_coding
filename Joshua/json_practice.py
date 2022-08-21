#step 1 import json library
import json 
a = {"name":"Joshua"}
#step 2: convert dict to string
a_str = json.dumps(a)
with open("Joshua_jsonfile.txt","w") as fd:
#step 3 save string in to txt file
    fd.write(a_str)

with open("Joshua_jsonfile.txt", "r") as fd:
    student_info = fd.read()
    print(student_info)
    #step 1 use json.loads(a) to convert str back to dict
    student_info = json.loads(student_info)
    student_info["name"] = "Jack"
    print(student_info)

my_dict = {"0001":{"Name":"Joshua", "Age": 10,"Gender":"Male","Chinese":89,"English":100, "Math":100}}

with open("Joshua_jsonfile.json",'w') as fd:
    json.dump(my_dict, fd, indent=4)