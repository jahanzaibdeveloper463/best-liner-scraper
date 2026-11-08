# Best liner scraper

A professional Python-based ETL (Extract, Transform, Load) script designed to scrape quote data from a live practice website. The application connects to the target host, extracts structured text, attributes authorship, parses keywords, and saves the cleaned dataset into an enterprise-ready CSV file.

## 🚀 Features

* **Targeted HTML Parsing:** Employs `BeautifulSoup` to navigate specific CSS classes (`.quote`, `.text`, `.author`, `.tag`) with high precision.
* **Resilient Networking:** Implements custom connection timeouts to prevent endless hangs during network anomalies.
* **Structured Data Export:** Transforms unstructured HTML nodes into a comma-separated format using Python's native `csv.DictWriter` module with full UTF-8 encoding support.
* **Console Visualization:** Outputs execution milestones (`[INFO]`, `[SUCCESS]`, `[DONE]`) alongside a terminal-based preview of the first three elements processed.

---

## 🛠️ Tech Stack & Requirements

* **Language:** Python 3.x
* **Core Libraries:** `beautifulsoup4`, `requests`
* **Standard Modules:** `csv`

---

## 🔧 Installation & Setup

1. **Clone or Download the Script:**
   Save the file locally as `scraper.py`.

2. **Install Required Libraries:**
   Execute the following command in your terminal to install the mandatory packages:
   ```bash
   pip install beautifulsoup4 requests
   ```

3. **Run the Script:**
   Execute the ETL pipeline directly:
   ```bash
   python scraper.py
   ```

---

## 💡 How It Works (Pipeline Architecture)

The logic follows a distinct, linear processing strategy wrapped entirely inside an active exception safety block:

### 1. The Extract Phase
The script requests access from `http://toscrape.com` using `requests.get()`. It explicitly checks for an HTTP status code `200 OK` before loading the raw webpage contents into the HTML parser.

### 2. The Transform Phase
The engine searches the parsed tree for all container nodes matching `<div class="quote">`. Iterating through these containers, it isolates three attributes:
* **Quote Body:** Stripped of trailing/leading whitespaces.
* **Author Name:** Cleaned and isolated text element.
* **Metadata Tags:** Pulled recursively, joined by commas, and mapped as a single flat string.

### 3. The Load Phase
A file handler opens `quotes_portfolio.csv` with explicit `utf-8` encoding. The script writes a standardized schema (`Quote`, `Author`, `Tags`) as headers, appends every extracted record, and closes safely.

---

## 📊 Sample Output Preview

### Terminal Console Log
```text
[INFO] Connecting to target website...
[SUCCESS] Found 10 quotes on the page. Extracting data...
[DONE] Data successfully saved to 'quotes_portfolio.csv'!
------------------------------------------------------------------
1. "The world as we have created it is a process of our thinking..." — *Albert Einstein*
2. "It is our choices, Harry, that show what we truly are..." — *J.K. Rowling*
3. "There are only two ways to live your life..." — *Albert Einstein*
------------------------------------------------------------------
```

### Generated CSV Layout (`quotes_portfolio.csv`)

| Quote | Author | Tags |
| :--- | :--- | :--- |
| The world as we have created it... | Albert Einstein | change, deep-thoughts, thinking, world |
| It is our choices, Harry... | J.K. Rowling | abilities, choices |

---

## ⚠️ Notes & Ethical Scraping Compliance
This script connects to a designated sandbox domain engineered specifically for testing automated scraping platforms. When pointing this logic toward live commercial hosts, ensure compliance with their `robots.txt` instructions and rate limits.
