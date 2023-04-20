import requests
import json
import time


# CoinMarketCap API URL for Matic
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

# API key for CoinMarketCap
api_key = 'YOUR_API_KEY'

# Parameters for the API request
parameters = {
  'symbol': 'MATIC',
  'convert': 'USD'
}

# Create a list to hold the data
data = []


# Make 60 API requests every minute
for i in range(60):
    # Make the API request
    response = requests.get(url, headers={'X-CMC_PRO_API_KEY': api_key}, params=parameters)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Get the data from the response
        response_json = json.loads(response.text)
        symbol = response_json['data']['MATIC']['symbol']
        open_timestamp = response_json['data']['MATIC']['quote']['USD']['open_timestamp']
        high_timestamp = response_json['data']['MATIC']['quote']['USD']['high_timestamp']
        low_timestamp = response_json['data']['MATIC']['quote']['USD']['low_timestamp']
        close_timestamp = response_json['data']['MATIC']['quote']['USD']['close_timestamp']
        
        # Add the data to the list
        data.append([symbol, open_timestamp, high_timestamp, low_timestamp, close_timestamp])
        
        # Wait for 1 minute
        time.sleep(60)
        
    else:
        print('Error: Connection problem')
        break
