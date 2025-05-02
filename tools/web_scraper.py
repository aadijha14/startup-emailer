from google.adk.tools import FunctionTool
import requests
from bs4 import BeautifulSoup

def scrape_website(url: str) -> dict:
    """
    Scrapes the given URL and returns extracted metadata.
    """
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            return {"error": f"Failed to fetch. Status: {response.status_code}"}

        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string.strip() if soup.title else "No title"
        meta_desc = soup.find("meta", attrs={"name": "description"})
        description = meta_desc["content"].strip() if meta_desc else "No description"

        return {
            "url": url,
            "title": title,
            "description": description
        }

    except Exception as e:
        return {"error": str(e)}

scrape_website_tool = FunctionTool(func=scrape_website)