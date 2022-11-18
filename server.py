from flask import Flask
import json 
from config import me 
from mock_data import catalog



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


@app.get("/api/catalogue")
def catlog():
    return json.dumps(catalog)


@app.get ("/api/test/count")
def Amount():
    return len(catalog)


@app.get("/api/catalog/<category>")
def by_category(category): 
    # category is to be replaced by a keyword in a URL, so if a keyword in "category" matches with the one placed in the url, it will display the page with the lists.
    results = []
    category = category.lower()
    for product in catalog:
        if product["category"].lower() == category:
            results.append(product)

    return json.dumps(results)


@app.get ("/api/catalog/search/<text>")
def by_search(text): 
    
    text = text.lower()
    results = []

    for searchItem in catalog:
        if text in searchItem["title"].lower() or text in searchItem["category"].lower():
            results.append(searchItem)

    return json.dumps(results)

@app.get ("/api/categories")
def cat_list():
    results = []
    for listItems in catalog:
        cat = listItems["category"]
        if cat not in results:
            results.append(cat)

    return json.dumps(results)

@app.get ("/api/test/price")
def price_list():
    total = 0
    for value in catalog:
        total = total + value["price"]
    
    return json.dumps(total)



    #create an endpoint that returns a poduct based on a given _id
@app.get ("/api/product/<id>")
def id(id):
    
    for identity in catalog:
        if identity["_id"] == id:
            return json.dumps(identity)

    return "error: Product not found"

app.run(debug=True)
