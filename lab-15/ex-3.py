filename = 'sample_txt.txt'
additional_text = "\nThis line is appended to the file."

# Append additional text to the file
with open(filename, 'a') as file:
    file.write(additional_text)
print(f"Additional text has been appended to {filename}")

# Read and print the updated file content
with open(filename, 'r') as file:
    updated_content = file.read()

print("Updated content of the file:")
print(updated_content)