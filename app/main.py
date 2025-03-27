from flask import Flask, request, render_template, send_file, redirect
import app.upload as upload
from app.scrapper import run_scraper
import os
app = Flask(__name__)

@app.route("/")
def home():
    # if 'auth' not in request.cookies:
    #     return redirect("/login", code=302)
    return render_template('index.html', current_page="home")

@app.route("/scrapper")
def scrapper():
    # return redirect("/", code=302)
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
    archive_url = run_scraper(urls)  # Assuming scrapper_func returns a file path
    
    return send_file(archive_url, as_attachment=True)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return {"status": "success"}


if __name__ == '__main__':
    host = f'127.0.100.100'

    os.system(f'start chrome {host}')
    app.run(host=host, port=80)
    
    
    
    
    
    