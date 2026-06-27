# Task 1: Web Scraping Amazon Mobiles using Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Step 1: Setup Chrome Driver
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# Step 2: Open Amazon Mobiles Page
url = "https://www.amazon.in/s?k=mobiles"
driver.get(url)
time.sleep(3)

# Step 3: Extract Data
names = []
prices = []
ratings = []
reviews = []

print("Scraping Amazon mobiles...")

products = driver.find_elements(By.CSS_SELECTOR, "div.s-result-item[data-component-type='s-search-result']")
print(f"Found {len(products)} products.")

for product in products:
    # Product Name
    try:
        name = product.find_element(By.CSS_SELECTOR, "h2 span").text.strip()
    except:
        name = "N/A"

    # Price
    try:
        price = "₹" + product.find_element(By.CSS_SELECTOR, "span.a-price-whole").text.strip().replace(",", "")
    except:
        price = "N/A"

    # Rating
    try:
        rating = product.find_element(By.CSS_SELECTOR, "span.a-icon-alt").get_attribute("innerHTML").strip()
        rating = rating.split(" ")[0]
    except:
        rating = "N/A"

    # Reviews
    try:
        review = product.find_element(By.CSS_SELECTOR, "span.a-size-base.s-underline-text").text.strip()
    except:
        review = "N/A"

    if name != "N/A":
        names.append(name)
        prices.append(price)
        ratings.append(rating)
        reviews.append(review)

driver.quit()

# Step 4: Save as CSV (Custom Dataset)
df = pd.DataFrame({
    "Product Name": names,
    "Price": prices,
    "Rating": ratings,
    "Reviews": reviews
})

df.to_csv("amazon_mobiles.csv", index=False)
print(f"✅ Saved: amazon_mobiles.csv")
print(f"Total Products: {len(df)}")
print(df.head(10))