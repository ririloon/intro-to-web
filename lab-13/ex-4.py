import re

text = "For more info, contact us at support@example.com or sales-info@example.org."

pattern =  r"\b\w+@\w+\.\w+\b"

emails = re.findall(pattern, text)

print("Email Addresses Found:", emails)
