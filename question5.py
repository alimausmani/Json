# Q5.Json string ko check karo ki vo complex object contain karti hai ya nahi?

import json 

obj={"a":12+3j,"b":12}
print(json.dumps(obj))