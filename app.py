import requests
from bs4 import BeautifulSoup

# Step 1: Send a request to the website
url = "https://quotes.toscrape.com/"
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract all quote texts
quotes = soup.find_all("span", class_="text")

print("Quotes from the website:\n")
for i, quote in enumerate(quotes, 1):
    print(f"{i}. {quote.text}")
