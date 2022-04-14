import json


def read_json(key):
    with open('test.json') as f:
        json_obj = json.load(f)
        try:
            return json_obj[key]
        except:
            return f"The key {key} doesn't exist"


print(read_json("education"))
