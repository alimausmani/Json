# 8.Tumhare pass four employes ki details hai list mai:-

# emp1=["neelam","programer","24","2400"]
# emp2=["komal","trainer","24","20000"]
# emp3=["anuradha","HR","25","40000"]
# emp4=["Abhishek","manager","29","63000"]

# # Visualize

# ab aapko 4 dictionaries create karni hai jaise ki emp1 emp2 emp3 and emp4.
# har ek employee ka dictionary main name,designation,age and salary honi chahiye.
# aur ye sab dictionary ki keys hai jismai maine list main value di hai. Iska use kar ke aapko ek json file create karni hai? Jaise ki niche diya hai.

# Output:-

# { 
#      "emp1":{ "name":"nilam",
#        "Designation":"programmer",
#        "Age":"34",
#        "salary":"24000",
#          }

#     "emp2":
#       { "name":"komal",
#         "Designation":"Trainee",
#         "Age":"24",
#         "salary":"20000" ,
#         }

 
#     "emp3":
#        { "name":"anuradha",
#          "Designation":"HR",
#          "Age":"25",
#          "salary":"40000",
#          }


#     "emp4":
#        { "name":"Abhishek",
#          "Designation":"Manager",
#          "Age":"29",
#        }
#  }

# emp1={"neelam","programer","24","2400"}

import json 
keys=["name","Degignation","age","salary"]
a=["nelam","programer","24","24000"]
emp1={}
emp2={}
emp3={}
emp4={}
dict={}
for i in range(len(keys)):
        emp1[keys[i]]=a[i]
        dict["employee1"]=emp1
        b=["komal","trainer","24","20000"]
        for i in range(len(keys)):
                emp2[keys[i]]=b[i]
                dict["employee2"]=emp2
                c=["anuradha","HR","25","40000"] 
        for i in range(len(keys)):
            emp3[keys[i]]=c[i]
            dict["employee3"]=emp3
            d=["Abhishek","manager","29","63000"]
        for i in range(len(keys)):
                emp4[keys[i]]=d[i]
                dict["employee4"]=emp4
                out_file=open("file.json","w")
                json.dump(dict,out_file,indent=6)
out_file.close()