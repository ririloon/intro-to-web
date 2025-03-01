import json

student_info = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science", "History"]
}

json_string = json.dumps(student_info, indent=4)

print("Serialized JSON string:")
print(json_string)