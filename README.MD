# TaskOn: data and file manipulation

This python script allows you to automate the process of retrieving data from a specific site, saving the results to a file, emailing it, and finally deleting the file. It will provide a convenient way to collect data, analyze it and share the results with others via email.

## Prerequisites
To run this script, you need to have the following installed:

- Python (version 3 or above),
- Requests library (install using 'pip install requests'),
- Jason library (included with Python),
- Time library (included with Python),
- CSV library (included with Python),
- OS library (included with Python)
- EmailMessage library (included with Python),
- an email account with SMTP access (e.g., Gmail, Outlook),
- API key (You will need to obtain a unique API key from CoinMarketCap to access their API. Visit the CoinMarketCap website and sign up for an account to obtain your API key).

## Configuration
Before running the script, you need to provide the necessary configuration in the TaskOn-data_and_file_manipulation.py file. Open the file in a text editor and set the following variables:

```python

# CoinMarketCap API URL
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

# API key for CoinMarketCap
api_key = 'your_unique_API_key'

# Define the file path and name
file_name = 'your_file_name.csv'
file_path = os.path.expanduser('your_file_path' + file_name)

# Set up email parameters
sender_email = 'your_email_address@example.com'
sender_password = 'your_email_password'
recipient_email = 'recipient_email_address@example.com'
email_subject = 'your_email_subject'
email_body = "your_message"

# SMTP server and SMTP port (e.g., for Gmail)
SMTP_SSL('smtp.gmail.com', 465)

```

Make sure to save the TaskOn-data_and_file_manipulation.py file after making the necessary changes.


## Usage
To use the script, follow these steps:

- Make sure you have completed the configuration step as mentioned above.
- Open a terminal or command prompt and navigate to the directory where the script is located.
- Run the script by executing the command: 

```bash
python3 TaskOn-data_and_file_manipulation.py
```

- The script will scrape the data from the specified website, process it, save the results to a file, send it via email, and delete the file.
- Check the recipient email account for the received email with the processed data.

## Future Features

Here are some potential features that you can consider adding to enhance the functionality of the script:

- Customizable Data Analysis: Allow users to specify their own data analysis tasks by accepting parameters or functions for processing the scraped data. This could include options for aggregations, filters, calculations, and visualizations.

- Scheduled Execution: Implement a scheduling mechanism (e.g., using Cron or a task scheduler library) to run the script automatically at specified intervals. This would allow you to retrieve and process the data periodically without manual intervention.

- Multiple Website Support: Extend the script to support scraping data from multiple websites by providing a configuration mechanism to specify different URLs, parameters, and processing logic for each website.

- Error Handling and Reporting: Enhance the error handling capabilities by implementing better exception handling, logging, and reporting mechanisms. This would provide detailed information about any failures or issues that occur during the execution of the script.

- Data Storage and Retrieval: Integrate a database or cloud storage solution to store the scraped data persistently. This would enable historical data analysis, data sharing, and more advanced data management capabilities.

## Disclaimer

Use this script responsibly and respect the terms of service of the website you are scraping data from. Make sure you have the necessary rights and permissions to retrieve and share the data. The authors of this script are not responsible for any misuse or illegal activities conducted with it.

## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)