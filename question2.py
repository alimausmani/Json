# Q.2 Python object ko json data main convert karne ka program likho?

# Example:
# Input :-
# Output:-
# {
#     "name": "David", 
#     "class": "I", 
#     "age": 6
# }

import json
d1="""{"name":"David",
 "class":"I",
 "age":6}"""
# x=json.dumps(d,indent=2)
# print(type(x))
# print(x)
y = open("Alima.json","w")
y.write(d1)
y.close()