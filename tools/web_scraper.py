from google.adk.tools import FunctionTool
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

def scrape_website(url: str) -> dict:
    """
    Scrapes the main URL and its top-level header links.
    Uses requests first, then falls back to Selenium.
    Returns metadata and cleaned text content from each page.
    """
    print(f"[DEBUG] scrape_website() called for: {url}")

    headers = {"User-Agent": "Mozilla/5.0"}
    page_texts = {}

    def fetch_html(u):
        try:
            response = requests.get(u, headers=headers, timeout=10)
            if response.status_code == 200:
                return response.text
        except Exception as e:
            print(f"[DEBUG] Requests failed for {u}: {e}")
        return None

    def fetch_with_selenium(u):
        print(f"[DEBUG] Falling back to Selenium for: {u}")
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=options)
        try:
            driver.get(u)
            html = driver.page_source
            return html
        except Exception as e:
            return f"[ERROR] Selenium failed: {str(e)}"
        finally:
            driver.quit()

    html = fetch_html(url)
    if not html:
        html = fetch_with_selenium(url)
        if "[ERROR]" in html:
            return {"error": html}

    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.string.strip() if soup.title else "No title"
    meta_desc = soup.find("meta", attrs={"name": "description"})
    description = meta_desc["content"].strip() if meta_desc else "No description"

    nav_links = set()
    for tag in soup.find_all('a'):
        href = tag.get("href")
        if href and not href.startswith(("mailto:", "tel:")):
            full_url = urljoin(url, href)
            if urlparse(full_url).netloc == urlparse(url).netloc:
                nav_links.add(full_url)

    for i, link in enumerate(list(nav_links)[:5]):
        sub_html = fetch_html(link)
        if not sub_html:
            sub_html = fetch_with_selenium(link)
        if "[ERROR]" in sub_html:
            page_texts[link] = sub_html
        else:
            sub_soup = BeautifulSoup(sub_html, "html.parser")
            text = sub_soup.get_text(separator=" ", strip=True)
            page_texts[link] = text  # Optional: text[:1500] to trim

    return {
        "main_url": url,
        "title": title,
        "description": description,
        "pages": page_texts
    }

scrape_website_tool = FunctionTool(func=scrape_website)