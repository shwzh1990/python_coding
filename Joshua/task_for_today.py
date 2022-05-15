#with open("123.txt","w") as fd:
#    fd.write("fdjkslafiewofl;sdajfiewfdshfiewhgflerghieorgheouriq")
#
#with open("123.txt","w") as fd:
#    fd.writelines(["1","2"])  #must be a list ...


import json
student = {"name":"Joshua"}

info = json.dumps(student)

with open("123.txt","w") as fd:
    fd.write(info)
