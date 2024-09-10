from flask import Flask, request, render_template, send_file, make_response
import upload
from scrapper import scrapper_func
import os
import time
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', current_page="home")

@app.route("/scrapper")
def scrapper():
    return render_template("scrapper.html", current_page='scrapper')

@app.route("/api", methods=["POST"])
def api():
    data: dict = request.get_json()
    url = upload.main(teletype_url=data['link'], name=data['name'], author_url=data['username'], boosty_auth=data.get("boosty_auth"))
    if url:
        return {"url": url}
    else:
        return 500



@app.route("/api/scrapper", methods=["POST"])
def scraper_api():
    data: dict = request.get_json()
    urls: list[str] = data['urls']  # Corrected the type declaration for urls
    archive_url = scrapper_func(urls)  # Assuming scrapper_func returns a file path
    resp = make_response(send_file(archive_url, as_attachment=True))
    
    # Use a custom header for file path
    resp.headers['X-Filename'] = archive_url
    return resp

@app.route("/api/scrapper/delete", methods=["POST"])  # Use POST for delete
def delete_temp_file():
    data: dict = request.get_json()
    path: str = data["path"]
    if os.path.exists(path):
        os.remove(path)
        return '', 200  # Return a proper HTTP status code
    else:
        return 'File not found', 404  # Handle file not found case



if __name__ == '__main__':
    host = f'127.0.100.100'

    # os.system(f'start chrome {host}')
    app.run(host=host, port=80)
    
    
    
    
    
    