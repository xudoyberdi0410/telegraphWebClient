import os
import time
import aiohttp
import asyncio
from aiofiles import open as aio_open
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from aiofiles import os as aio_os


async def fetch_image(session, url, folder_path, index):
    async with session.get(url) as response:
        content_type = response.headers.get('Content-Type', 'image/jpeg')
        ext = content_type.split('/')[1] if '/' in content_type else 'jpg'
        img_name = f"{index}.{ext}"
        img_data = await response.read()
        async with aio_open(os.path.join(folder_path, img_name), 'wb') as img_file:
            await img_file.write(img_data)


async def scrape_page(session, url, folder_path):
    async with session.get(url) as response:
        text = await response.text()
        soup = BeautifulSoup(text, "lxml")
        images_tags = soup.find_all("img")
        tasks = []
        for index, item in enumerate(images_tags, start=1):
            img_url = urljoin(url, item['src'])
            tasks.append(fetch_image(session, img_url, folder_path, index))
        await asyncio.gather(*tasks)


async def scraper_func(urls):
    main_folder_name = str(time.time())
    main_folder = os.path.abspath(main_folder_name)
    await aio_os.mkdir(main_folder)
    async with aiohttp.ClientSession() as session:
        tasks = []
        for index, url in enumerate(urls, start=1):
            sub_folder = os.path.join(main_folder, str(index))
            await aio_os.mkdir(sub_folder)
            tasks.append(scrape_page(session, url, sub_folder))
        await asyncio.gather(*tasks)


def run_scraper(urls):
    asyncio.run(scraper_func(urls))


# # Example usage
# urls = [
#     'https://example.com/page1',
#     'https://example.com/page2',
# ]
# run_scraper(urls)
