import re

text = "An apple a day keeps the doctor away. Even elephants enjoy eating."

pattern = r"\b[aeiou]\w*\b"

vowel_words = re.findall(pattern, text, re.IGNORECASE)

print("Words starting with a vowel:", vowel_words)
