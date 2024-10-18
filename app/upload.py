from telegraph import Telegraph

from app.parser import parser

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

def main(teletype_url: str, name: str, author_url: str, boosty_auth: str = None):
    teletype_answer = parser(teletype_url, boosty_auth)
    try:
        content = ''.join([f'<img src="{url}">' for url in teletype_answer.urls])
        return createPage(acess_token=access_token, title=teletype_answer.title, author_name=name, author_url=author_url, content=content)
    except Exception as ex:
         return None
if __name__ == "__main__":
    main()