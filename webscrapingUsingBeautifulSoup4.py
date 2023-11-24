# Install necessary libraries
# pip install requests beautifulsoup4 pandas

import requests
from bs4 import BeautifulSoup
import pandas as pd
import textwrap


def justify_text(text, width=100):
    """Justify the text by wrapping it to a specified width."""
    return textwrap.fill(text, width)


# Specify the URL you want to scrape
url = "https://medium.com/@swarnimshukla_78236/embracing-the-fight-of-life-overcoming-setbacks-and-achieving-success-7a66e313a04e"

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the text data you need
    # Inspect the HTML structure of the website
    # and adjust the selectors accordingly
    data_elements = soup.select('.er')

    # Create a list to store the extracted text data
    text_data = [element.get_text() for element in data_elements]

    # justify text data
    justified_text_data = [justify_text(text) for text in text_data]

    # Create a pandas DataFrame from the list
    df = pd.DataFrame({'Text Data': justified_text_data})
    df.to_csv('justified_op.csv', index=True)

    print("Data has been scraped and saved to 'output.xlsx'")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
