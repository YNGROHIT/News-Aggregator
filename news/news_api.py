import requests

# Replace with your actual NewsAPI key
API_KEY = '5785a932284341849ab72c63e81bd914'  # You can replace 'your_newsapi_key_here' with your actual API key
API_URL = 'https://newsapi.org/v2/top-headlines'

def get_top_headlines(category='general', country='us'):
    params = {
        'country': country,  # You can change the country code (e.g., 'in' for India)
        'category': category,  # You can change the category (e.g., 'technology', 'business', etc.)
        'apiKey': API_KEY,  # Your NewsAPI key
    }
    
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the response in JSON format
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return {'articles': []}  # Return an empty list of articles in case of an error
