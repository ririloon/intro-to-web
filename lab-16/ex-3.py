import json

student_info = {
    "name": "Alice",
    "age": 21,
    "course": ["Math", "Science", "History"]
}

filename = 'student.json'

with open(filename, 'w') as file:
    json.dump(student_info, file, indent=4)
print(f"Data has been written to {filename}")

with open(filename, 'r') as file:
    data_loaded = json.load(file)

print("Data loaded from JSON file:")
print(data_loaded)