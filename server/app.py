from flask import Flask, jsonify, request
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

app = Flask(__name__)
CORS(app)

def scrape_amazon_products(url):
    # Set up Chrome options for Selenium
    options = Options()
    options.add_argument("--headless")  
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Set up Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # Initialize empty list to store product data
    products = []
    page_num = 1
    max_pages = 100

    while page_num <= max_pages:
        # Load the page
        page_url = f"{url}&page={page_num}"
        print(f"Scraping page {page_num}: {page_url}")
        driver.get(page_url)
        time.sleep(2)  
        
        # Locate product elements
        product_elements = driver.find_elements("css selector", "div.s-main-slot div.s-result-item")
        # Stop if no products are found
        if not product_elements:  
            print("No more products found, stopping.")
            break
        
        # Loop through products and extract details
        for product in product_elements:
            product_data = {}
            try:
                name = product.find_element("css selector", "h2 span").text
                product_data["Product Name"] = name if name != "N/A" else None
            except:
                product_data["Product Name"] = None

            try:
                price = product.find_element("css selector", "span.a-price-whole").text
                product_data["Price"] = price if price != "N/A" else None
            except:
                product_data["Price"] = None
            
            try:
                rating = product.find_element("css selector", "span.a-icon-alt").get_attribute("innerHTML")
                product_data["Rating"] = rating if rating != "N/A" else None
            except:
                product_data["Rating"] = None
            
            try:
                seller = product.find_element("css selector", "span.a-size-base.a-color-secondary").text
                product_data["Seller Name"] = seller if seller != "N/A" else None
            except:
                product_data["Seller Name"] = None

            # Only add product to list if required data exists
            if all(value not in [None, "", "N/A"] for value in product_data.values()):
                products.append(product_data)

        page_num += 1  

    # Close the driver
    driver.quit()

    
    df = pd.DataFrame(products)
    if df.empty:
        print("No valid data to save.")
        return []

    # Clean the data: Remove entries with empty or 'N/A' values
    df = df.dropna()
    df = df.loc[~df.isin(["N/A"]).any(axis=1)]

    # Save to CSV
    try:
        df.to_csv("amazon_products.csv", index=False)
        print("CSV file created successfully.")
    except Exception as e:
        print(f"Error saving CSV: {e}")

    return products

# Define the Flask route for scraping
@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.json.get("url")
    if not url:
        return jsonify({"error": "URL is required"}), 400
    
    
    try:
        data = scrape_amazon_products(url)
        if not data:
            return jsonify({"error": "No valid products found"}), 404
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)