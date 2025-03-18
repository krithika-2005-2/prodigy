import requests
from bs4 import BeautifulSoup
import pandas as pd

# Amazon Scraper API (Replace with your API key)
API_KEY = "your_scraperapi_key"
URL = "https://www.amazon.in/s?k=laptops+under+70000"

# Use ScraperAPI to bypass Amazon's bot detection
SCRAPER_URL = f"http://api.scraperapi.com?api_key={API_KEY}&url={URL}&render=true"

# Function to get the HTML content of the page
def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

# Function to parse the HTML content and extract product information
def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    products = []

    for item in soup.select('.s-main-slot .s-result-item'):
        name = item.select_one("h2 a span")
        price_whole = item.select_one(".a-price-whole")
        price_fraction = item.select_one(".a-price-fraction")
        rating = item.select_one(".a-icon-alt")

        name = name.get_text(strip=True) if name else "No name available"
        price = f"{price_whole.get_text(strip=True)}.{price_fraction.get_text(strip=True)}" if price_whole and price_fraction else "No price available"
        rating = rating.get_text(strip=True) if rating else "No rating available"

        products.append({
            'name': name,
            'price': price,
            'rating': rating
        })

    return products

# Function to save the extracted product information to a CSV file
def save_to_csv(products, filename='products.csv'):
    df = pd.DataFrame(products)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

# Main script
html_content = get_html(SCRAPER_URL)
if html_content:
    products = parse_html(html_content)
    save_to_csv(products)
