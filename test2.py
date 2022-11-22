from flask import Flask
import json

ages = [12, 34, 15, 73, 73, 13, 97, 23, 95,
        23, 98, 53, 83, 45, 90, 23, 75, 23, 78]


arr = ages[0]
for product in ages:
    if product > arr:
        arr = product

print(arr)

# print(max(arr)) can work as well
