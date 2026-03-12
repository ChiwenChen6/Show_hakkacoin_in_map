### README.md
中文版　README_zh-Hant.md

# Hakka Coin Store Scraper

A robust **Selenium-based** web scraper designed to collect partner store information from the [Hakka Coin Official Website](https://www.hakkacoin.com.tw/store).

## 🚀 Key Features
* **Auto-Pagination**: Automatically detects and clicks the "Next" button until all pages are processed.
* **Dynamic Content Handling**: Uses `WebDriverWait` and state detection to ensure data integrity during page transitions.
* **Error Resilience**: Wrapped in comprehensive `try-except` blocks to prevent crashes from network timeouts.
* **Data Export**: Cleans duplicate entries and exports results to a CSV file (`utf-8-sig` encoding for Excel compatibility).

## 🛠️ Setup & Installation
Ensure you have Python 3.8+ installed, then run:
```bash
pip install selenium webdriver-manager pandas
```
🖥️ Usage
Run the script:

Bash
python your_script_name.py
The program will launch a Chrome instance and begin scraping.

Upon completion, the data will be saved as hakka_stores_final.csv in the same directory.


https://www.google.com/maps/d/edit?mid=1c3FmHENEzsQuzT6iazjT7dWbb4kzgZ4&ll=24.90753179767694%2C121.19737290185861&z=12
