import requests
from lxml import etree


def prepare_url(author, title):
    url = f"https://www.songlyrics.com/{author}/{title}-lyrics/"
    url = url.replace(" ", "-").lower()
    
    return url


def scrap_lyrics(author, title):
    try:
        url = prepare_url(author, title)
        response = requests.get(url)
        response.raise_for_status()

        html = etree.HTML(response.content)
        text = html.xpath("string(//div[@id='songLyricsDiv-outer'])")

        if text:
            return text.strip()

        return ""

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return ""
