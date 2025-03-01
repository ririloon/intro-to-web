import re

text = "There are 3 apples, 15 oranges, and 256 bananas in the basket."

pattern = r"\d+"

result = re.sub(pattern, "NUMBER", text)

print("Modified Text:", result)
