import json

x = json.dumps(["Colombia", 'South America', 45000000])
print(x)

#you can provide different types in json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None)) 

# to load a file with json format
countriesfile = open("C:\\Desarrollo\\PythonScripts\\7_Input_Output\\countries.json")
countries_json = json.load(countriesfile)

for c in countries_json:
    print(c["country"])