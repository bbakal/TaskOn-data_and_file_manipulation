import prvdt
import requests
import json
import time
import csv
import os
from email.message import EmailMessage



# CoinMarketCap API URL for Matic
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

# API key for CoinMarketCap
api_key = prvdt.my_api_key

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
    
# Save the data in a CSV file
with open('matic_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Symbol', 'Open Timestamp', 'High Timestamp', 'Low Timestamp', 'Close Timestamp'])
    for row in data:
        writer.writerow(row)

# Set up email parameters
sender_email = 'your_email_address@example.com'
sender_password = 'your_email_password'
recipient_email = 'recipient_email_address@example.com'
email_subject = 'MATIC Today'
email_body = "I am sending today's data on the MATIC cryptocurrency."

# Define the file path and name
file_name = 'matic_data.csv'
file_path = os.path.expanduser('~/Pulpit/' + file_name)

# Create a message object
msg = EmailMessage()
msg['Subject'] = email_subject
msg['From'] = sender_email
msg['To'] = recipient_email
msg.set_content(email_body)


