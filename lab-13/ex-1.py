import re

text = "Call me at 555-1234 or at the office line 555-5678. For emergencies, dial 555-9999."

pattern = r"\d{3}-\d{4}"

phone_numbers = re.findall(pattern, text)

print("Phone Numbers Found:", phone_numbers)
