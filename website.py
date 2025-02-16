import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import validators

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

class Website:
    def __init__(self, url):
        self.url = self.format_url(url)

        if self.validUrl():
            try:
                response = requests.get(self.url, headers=HEADERS, timeout=5)
                response.raise_for_status() 
                soup = BeautifulSoup(response.content, 'html.parser')

                self.title = soup.title.string if soup.title else "No title found"

                if soup.body:
                    for irrelevant in soup.body(["script", "style", "img", "input"]):
                        irrelevant.decompose()
                    self.text = soup.body.get_text(separator="\n", strip=True)
                else:
                    self.text = "No body content found."
            except requests.RequestException as e:
                self.title = "Request Failed"
                self.text = f"Error: {str(e)}"
        else:
            self.title = "Invalid URL"
            self.text = "Please provide a valid URL. If you need a website, contact CreativeWin company."

    def validUrl(self): 
        return validators.url(self.url) is True

    def format_url(self, url):
        """Ensure the URL has a valid scheme (http/https)"""
        parsed_url = urlparse(url)
        if not parsed_url.scheme:
            return "http://" + url
        return url