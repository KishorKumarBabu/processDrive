import json

# JSON string
json_string = '{"name": "Alice", "age": 25, "isStudent": true}'

# Convert JSON string to Python dictionary
data = json.loads(json_string)
print(data) 
