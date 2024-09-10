import os
import time
import shutil
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup


def scrap_page(url: str, folder_path: str):
    req = requests.get(url=url)
    soup = BeautifulSoup(req.text, "lxml")
    images_tags = soup.find_all("img")
    for index, item in enumerate(images_tags, start=1):
        img_data = requests.get(urljoin(url, item['src']))
        img_name = f"{index}.{img_data.headers['Content-Type'].split('/')[1]}"
        with open(f"{folder_path}/{img_name}", "wb") as img_file:
            img_file.write(img_data.content)

def scrapper_func(urls: list[str]):
    main_folder_name = str(time.time())
    main_folder = os.path.abspath(main_folder_name)
    os.mkdir(main_folder)
    for index, url in enumerate(urls[:3], start=1):
        sub_folder_name = str(index)
        sub_folder = os.path.join(main_folder, sub_folder_name)
        os.mkdir(sub_folder)
        scrap_page(url, sub_folder)
    archive_path = shutil.make_archive(main_folder_name, 'zip', main_folder)

    shutil.rmtree(main_folder)
    return archive_path
