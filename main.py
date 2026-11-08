from bs4 import BeautifulSoup
import csv
import requests

# Target practice website
URL = "http://quotes.toscrape.com/"


def scrape_quotes():
  print("[INFO] Connecting to target website...")
  try:
    response = requests.get(URL, timeout=10)
    # Check if request was successful
    if response.status_code != 200:
      print(f"[ERROR] Failed to retrieve page. Status code: {response.status_code}")
      return

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all quote boxes on the page
    quote_boxes = soup.find_all("div", class_="quote")
    print(
        f"[SUCCESS] Found {len(quote_boxes)} quotes on the page. Extracting"
        " data..."
    )

    scraped_data = []

    for box in quote_boxes:
      # Extract Quote Text
      text = box.find("span", class_="text").get_text(strip=True)

      # Extract Author
      author = box.find("small", class_="author").get_text(strip=True)

      # Extract Tags associated with the quote
      tags = [tag.get_text(strip=True) for tag in box.find_all("a", class_="tag")]
      tags_str = ", ".join(tags)

      scraped_data.append({"Quote": text, "Author": author, "Tags": tags_str})

    # Save data into a clean CSV file
    file_name = "quotes_portfolio.csv"
    with open(file_name, mode="w", newline="", encoding="utf-8") as file:
      fieldnames = ["Quote", "Author", "Tags"]
      writer = csv.DictWriter(file, fieldnames=fieldnames)

      writer.writeheader()
      for item in scraped_data:
        writer.writerow(item)

    print(f"[DONE] Data successfully saved to '{file_name}'!")
    print(
        "------------------------------------------------------------------"
    )
    for i, item in enumerate(scraped_data[:3], 1):
      print(f"{i}. \"{item['Quote']}\" — *{item['Author']}*")
    print(
        "------------------------------------------------------------------"
    )

  except Exception as e:
    print(f"[ERROR] An error occurred: {e}")


if __name__ == "__main__":
  scrape_quotes()
