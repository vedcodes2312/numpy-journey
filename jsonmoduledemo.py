import json
import sys
#json - javascript object notation
# python object

sample = {
    "name":"xyz",
    "age":20,
    "skills":["python","aiml"]
}

# python object to json string

jsonstr = json.dumps(sample)

# json string to python object

pythonobj = json.loads(jsonstr)
print(jsonstr)
print(f"{sample}")
print(f"{pythonobj}")

print(type(sample), type(jsonstr),type(pythonobj))

#json str has string class 

print(sys.getsizeof(jsonstr))


# dumps is also called serialization
data = {
    "name": "Alice",
    "age": 25,
    "is_student": True,
    "courses": ["Math", "Science"],
    "address": None
}

# Convert Python dict to JSON string
json_string = json.dumps(data)
print(json_string)

# formatted op
json_formatted = json.dumps(data, indent=4)
print(json_formatted)
