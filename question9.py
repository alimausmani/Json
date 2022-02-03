# Q.9 Apki pass ek shopping name ki ek dictionary hai
# {
#     "shopping_list":
#         { 
#             "chaco":"15",
#             "Biscuits":"50",
#             "Diary_milk":"30",
#             "ice_cream":"20",
#         } 

# Apki dictionary ka use kar ke ek json file create karna hai.
# Aur apko kuch task perform karne hai jaise ki
# 1
# main dekhna chahta hu shopping list ko json file dekhna.
# 2
# phir main user se poochu ga ki kon sa item khareedna chahte ho.
# 3
# uske baad user name dega phir user se input poochege jaise ki tum kitne item chahte ho.
# 4
# phir aapka wo number of items json file se remove karna hai.
# 5
# Agar tumhe shopping items add karna hai to tumko json file main insert karna hoga.
# Output:-
# show shopping_list:- 
# {
#     "shopping_list":{ 
#         "chaco":"15",
#         "Biscuits":"50",
#         "Diary_milk":"30",
#         "ice_cream":"20",
#          } 
# }

from importlib.abc import InspectLoader
import json
A={"shoping_list":
{
    "chaco":"15",
    "Biscuits":"50",
    "Dairy_milk":"30",
    "ice_cream":"20"
    }
}

G=input("enter the item:")
P=int(input("enter the quantity:"))
for i in A:
    for g in A[i]:
        if G not in A[i]:
            print(G,"Not available")
            break
        elif int(A[i][g])<P and  g==G:
            print("Not available")
            break
        elif g==G and int(A[i][g])>P:
            b=int(A[i][g])-P
            A[i][g]=str(b)
            break
with open("Asra Usmani.json","w") as write_file:
    json.dump(A,write_file,indent=4)
with open("Asra Usmani.json","r") as read_file:
    c = read_file.read()
print(c)
print(type(c))                


