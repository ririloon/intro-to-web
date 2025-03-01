import re

text1 = "Hello, world! Welcome to regex."
text2 = "Greetings! Hello, how are you?"

pattern = r"Hello"

match1 = re.match(pattern, text1)
print("Using re.match() on text1:")
if match1:
    print("Match found:", match1.group())
else:
    print("No match found.")

match2 = re.match(pattern, text2)
print("\nUsing re.match() on text2:")
if match2:
    print("Match found:", match2.group())
else:
    print("No match found.")

search_result = re.search(pattern, text2)
print("\nUsing re.search() on text2:")
if search_result:
    print("Found:", search_result.group())
else:
    print("No match found.")
