import requests

# Example API endpoint (this is a dummy URL for demonstration purposes)
api_url = "https://api.example.com/weather"

# Parameters for the API request, such as the city name and API key (if required)
params = {
    "city": "New York",
    "apikey": "your_api_key_here"
}

# Make a GET request to the API
response = requests.get(api_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    weather_data = response.json()  # Convert JSON response to a Python dictionary
    print("Current Weather Data:")
    print(weather_data)
else:
    print("Failed to retrieve data. Status code:", response.status_code)
