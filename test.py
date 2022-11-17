from flask  import Flask
import  json
from config import me

#print example --> print(me["first"]) or print me(["first"] + " " + me["last"])
print(me["first"]) 
#value modification --> me[:"first"] = "Kenny"
me["first"] = "Kenny"
print(me["first"])
#add new keys and values --> me["prefferred color"] ="gray"




me["prefferred color"] ="gray"
print(me)


address = me["address"]
print(address["area"]) + " " + address ["city"] + " " + address["state"] 
print(str(address["street"]))
#use print(str(address["street"]) to turn a value iinto a string