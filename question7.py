# Q7.Text file data ko json file data mai convert karo,jaise ki neeche diya hai?

# Example:

# Input :-


# Text.txt:- 

# Visualize

# Output:-

# Json_file.json:-

# {
#     “Name”: “Abhishek”,
#     “Designation”: “CEO of      navgurukul”,
#     “Gender”:”male”,
#     “Age”: “29”
#     }



# Name Abhishek
#  Designation CEO of navgurukul
#  Gender male
#  Age 29



import json

dic={"Name":"Abhishek","Designation":"CEO of navgurukul","Gender":"male","Age":"29"}
json_obj=json.dumps(dic,indent=2)
with open("Text.txt.json","w") as f:
    f.write(json_obj)
    f.close()
f = open("Text.txt.json","r")
a=f.read()
print(a)

  