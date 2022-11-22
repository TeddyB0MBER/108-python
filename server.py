from flask import Flask, request, abort
import json
import random
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
        "v": "v1.0.4",
        "name": "zombie rabbit"
    }
# parse a dictionary into a json string  for storage
    return json.dumps(version)


@app.get("/api/about")
def Info():
    return json.dumps(me)


@app.get("/api/catalogue")
def catlog():
    return json.dumps(catalog)


@app.post("/api/catalogue")
def save_product():
    product = request.get_json()

    # validations
    # in statements is used to check for a  specific definition in an array
    if "title" not in product:
        return abort(400, "Title is required")
    if len(product["title"]) < 5:
        return abort(400, "title should contain 5 chars or mroe")
    if "category" not in product:
        return abort(400, "Category is required")
    if "price" not in product:
        return abort(400, "Price is required")
    if not isinstance(product["price"], (float, int)):
        return abort(400, "Price must be a valid number")
    if product["price"] < 0:
        return abort(400, "price must be greater then 0")

    product["_id"] = random.randint(1000, 10000)

    catalog.append(product)

    return json.dumps(product)


@app.get("/api/test/count")
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


@app.get("/api/catalog/search/<text>")
def by_search(text):

    text = text.lower()
    results = []

    for searchItem in catalog:
        if text in searchItem["title"].lower() or text in searchItem["category"].lower():
            results.append(searchItem)

    return json.dumps(results)


@app.get("/api/categories")
def cat_list():
    results = []
    for listItems in catalog:
        cat = listItems["category"]
        if cat not in results:
            results.append(cat)

    return json.dumps(results)


@app.get("/api/test/price")
def price_list():
    total = 0
    for value in catalog:
        total = total + value["price"]

    return json.dumps(total)

    # create an endpoint that returns a poduct based on a given _id


@app.get("/api/product/<id>")
def id(id):

    for identity in catalog:
        if identity["_id"] == id:
            return json.dumps(identity)

    return "error: Product not found"

# this endpoint will run through the array and return the cheapest product.


@app.get("/api/sort/cheapest")
def cheap():

    arr = catalog[0]
    for product in catalog:
        if product["price"] < arr["price"]:
            arr = product

    return json.dumps(arr)


app.run(debug=True)
