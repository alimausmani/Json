# Q4.Python dictionary(sort by key) object ko json data ::mai convert karne ka program likho?

# Example:
# Input :-
# {
#     '4': 5, 
#     '6': 7, 
#     '1': 3, 
#     '2': 4}
# Output:-
# JSON data:
# {
#     "1": 3,
#     "2": 4,
#     "4": 5,
#     "6": 7
# }




import json
json_data={
    '4':5,
    '6':7,
    '1':3,
    '2':4}   
y=open("Usmani Alima.json","w") 
y.write((json.dumps(json_data, sort_keys=True, indent=4)))
y.close()   