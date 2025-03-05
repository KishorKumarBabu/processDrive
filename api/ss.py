import jsonify



def complex():
    data = {
        "name": "John",
        "age": 30,
        "friends": [
            {"name": "Doe", "age": 25},
            {"name": "Smith", "age": 28}
        ]
    }
    return jsonify(data)

print(complex)