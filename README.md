# Quotes Web Scraper

## Project Overview
This project is a simple **Python web scraping script** that extracts quotes from the website [Quotes to Scrape](https://quotes.toscrape.com/). The script uses `requests` to fetch the HTML content and `BeautifulSoup4` (bs4) to parse and extract the data.  

Web scraping allows automatic collection of data from websites instead of manually copying it, which can be useful for data analysis, research, automation, and building datasets for ML projects.

---

## Features
- Fetches quotes from the homepage of the website.
- Prints all quotes to the console.
- Can be extended to save quotes to CSV or Excel.
- Can be enhanced to scrape authors, tags, and multiple pages.

---

## Technologies Used
- **Python 3**
- **Requests** – to send HTTP requests to websites
- **BeautifulSoup4 (bs4)** – to parse and extract HTML data
- **pandas** (optional) – to save scraped data to CSV/Excel

---

## Installation
**1. Clone the repository:**
   ```bash
   git clone https://github.com/anujatappeta/Web_scraping.git
```
**2.Navigate to the project folder:**
    
   cd Web_scraping

**3.Install required Python packages:**
      
   pip install requests beautifulsoup4

**4.Open app.py in your IDE (VS Code, PyCharm, etc.).**
      
**Run the script:**
python app.py
