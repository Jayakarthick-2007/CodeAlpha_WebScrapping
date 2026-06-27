# CodeAlpha_WebScrapping
A Python-based web scraper that extracts mobile product data (name, price, rating, reviews) from Amazon using Selenium WebDriver and BeautifulSoup. Automates browser navigation, handles dynamic web pages, and saves the collected data into a structured CSV dataset.
# 🕷️ Web Scraping — Amazon Mobile Products

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Purpose](https://img.shields.io/badge/Purpose-Educational-purple)

## 📌 Overview
This project automates the extraction of mobile product information
from Amazon's search results and stores it as a structured CSV dataset
for further analysis.

---

## 🚀 Features
- ✅ Automated browser navigation using Selenium WebDriver
- ✅ Extracts product name, price, rating, and customer reviews
- ✅ Handles dynamic web pages loaded via JavaScript
- ✅ Anti-bot detection bypass techniques
- ✅ Saves scraped data into structured CSV format
- ✅ Error handling for missing or unavailable elements

---

## 🛠️ Technologies Used
| Tool | Purpose |
|---|---|
| Python 3 | Core programming language |
| Selenium WebDriver | Browser automation |
| BeautifulSoup | HTML parsing |
| Pandas | Dataset creation |
| WebDriver Manager | Auto ChromeDriver setup |

---

## 📦 Installation

**Step 1** — Clone the repository:
git clone https://github.com/yourusername/web-scraping-amazon-mobiles.git
**Step 2** — Navigate to project folder:
cd web-scraping-amazon-mobiles
**Step 3** — Install required libraries:
pip install selenium webdriver-manager beautifulsoup4 pandas
**Step 4** — Run the scraper:
python amazon_task1.py
---

## 📁 Output
| File | Description |
|---|---|
| `amazon_mobiles.csv` | Scraped dataset with product details |

---

## 📊 Dataset Columns
| Column | Description |
|---|---|
| Product Name | Name of the mobile product |
| Price | Price in ₹ (Indian Rupees) |
| Rating | Star rating out of 5 |
| Reviews | Number of customer reviews |

---

## 🔄 Project Workflow
1. Selenium opens Chrome browser automatically
2. Navigates to Amazon mobile search results page
3. Locates and extracts product details from HTML elements
4. Stores extracted data into a Pandas DataFrame
5. Exports final dataset as CSV file

---

## 💡 No-Code Alternative
Tools like **Octoparse** and **ParseHub** can perform the same
scraping task visually without writing any code.

---

## ⚠️ Disclaimer
This project is built strictly for **educational purposes only**.
Always check a website's terms of service before scraping.

---

## 👨‍💻 Author
- **Name:** JAYAKARTHICK A
- **LinkedIn:** www.linkedin.com/in/a-jayakarthick-5036a334a
- **GitHub:** https://github.com/Jayakarthick-2007/CodeAlpha_WebScrapping


