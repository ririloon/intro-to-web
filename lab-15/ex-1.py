filename = 'sample_txt.txt'
content = """Hello, world!
This is a sample text file.
It contains multiple lines of text for testing file operations."""

# Write the content to the file
with open(filename, 'w') as file:
    file.write(content)
print(f"Content has been written to {filename}")

# Read the content back from the file
with open(filename, 'r') as file:
    read_content = file.read()

print("Content read from file:")
print(read_content)
