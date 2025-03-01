from datetime import datetime

now = datetime.now()

formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print("Current Dte and Time:", formatted_now)