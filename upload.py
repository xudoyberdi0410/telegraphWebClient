import requests
import json
from tqdm import tqdm
import time
from telegraph import Telegraph
from werkzeug.datastructures import FileStorage

access_token = '4a6d722e42a2f20c264786aa49ce32b219260dcd1c6b5f4564f8efb78a39'

def createPage(acess_token: str, title: str, author_name: str, author_url: str, content: list):
    telegraph = Telegraph(access_token=acess_token)
    response = telegraph.create_page(
        title=title,
        html_content=content,
        author_name=author_name,
        author_url=author_url
    )
    return response['url']

    
def telegraph_file_upload(images: list[FileStorage]):
    urls = []
    try:
        for image in tqdm(images, 'Uploading images to server telegra.ph'):            
            url = 'https://telegra.ph/upload'
            response = requests.post(url, files={'file': ('file', image.read(), image.headers['Content-Type'])})
            
            telegraph_url = json.loads(response.content)
            telegraph_url = telegraph_url[0]['src']
            telegraph_url = f'https://telegra.ph{telegraph_url}'
            
            urls.append(telegraph_url)
            time.sleep(3)
    except KeyError as e:
            print(f'Telegraph url: {telegraph_url}\nImage: {image.filename}')
            print(e)
            return -1
        
    return urls

def main(images: list[FileStorage], title: str, name: str):
    image_urls = telegraph_file_upload(images)
    content = ''.join([f'<img src="{url}">' for url in image_urls])
    return createPage(acess_token=access_token, title=title, author_name=name, author_url='https://t.me/khudoberdi0410', content=content)

if __name__ == "__main__":
    main()