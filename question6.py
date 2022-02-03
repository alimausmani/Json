# Q6.Python object key unique key value ko access karne ka program likho?
# Example:
# Input :-
# '{
#  "a":  1,
#  "a":  2,
#  "a":  3, 
#  "a": 4,   
#  "b": 1, 
#  "b": 2
#  }'

# Output:-
# Original Python object:- 
# {
#     "a":  1, 
#     "a":  2, 
#     "a":  3, 
#     "a": 4, 
#     "b": 1, 
#     "b": 2
# }
# Unique Key in a JSON object:-
# {'a': 4, 'b': 2}

data={
    "a":1,
    "a":2,
    "a":3,
    "a":4,
    "b":1,
    "b":2
    }
# print ("Original dictionary is : " + str(data)) 
b={}
for i in data:
    b.update(data)
print("Unique key in a json object",b)
