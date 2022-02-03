"""Q.1 Json data ko python object main convert karne ka program likho?.
Example:
Input :-
Output :-"""



import json 
d='{"Alima":"Usmani","Class":"12","Subject":"sciencee"}'
y = open("alima.json","w")
y.write(d)
y.close()


# x=json.loads(d)
# print(x)

# for a in x:
#     print(a,x[a])


