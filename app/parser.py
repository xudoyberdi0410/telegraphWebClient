import requests
from bs4 import BeautifulSoup as bs
import json

class ParserAnswer:
    def __init__(self, title: str, urls: list[str]) -> None:
        self.title = title
        self.urls = urls


def parser(url: str, boosty_auth: str = None) -> ParserAnswer:
    cookies = {
        "auth": boosty_auth
    }
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-GB,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
    if "wamanga" in url:
        url = url.replace("/read", "/api/read")
    req = requests.get(url=url, headers=headers, cookies=cookies)
    soup = bs(req.text, "lxml")
    if "teletype" in url:
        title = soup.find("h1").text.encode('latin1').decode('utf-8')
        urls = [i['src'] for i in soup.find_all("img")]
        
        return ParserAnswer(title=title, urls=urls)
    elif "wamanga" in url:
        data = req.json()
        urls = data.get("chapter").get("pages")
        title = data.get("chapter").get("full_title")
        return ParserAnswer(title=title, urls=urls)
        # with open("./parser_test.json", "w", encoding="utf-8") as f:
        #     f.write(req.text)
        return
    script_tag = soup.find("script", {"id": "initial-state"}).text
    script_tag: dict = json.loads(script_tag)
    urls = []
    for i in script_tag["posts"]["postsList"]["data"]["posts"][0]["data"]:
        if i["type"] == "image":
            urls.append(i["url"])
    title = soup.find("h1").text
    return ParserAnswer(title=title, urls=urls)

if __name__ == "__main__":
    parser("https://wamanga.ru/read/kanojo-okarishimasu/ru/ch/349#1")
    