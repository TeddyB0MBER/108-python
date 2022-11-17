from flask import Flask
import json 
from config import me 



app = Flask("server")


@app.get("/")  # the root endpoint
def home():
    return "hello from flask"



@app.get("/test")
def test():
    return "this is another endpoint"


#  CATALOG API 

@app.get("/api/version")
def version():
    version = {
        "v":"v1.0.4",
        "name":"zombie rabbit"
    }
# parse a dictionary into a json string  for storage
    return json.dumps(version)



@app.get("/api/about")
def Info():
   return json.dumps(me)

app.run(debug=True)
