from flask import Flask, request, render_template
import upload
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/api", methods=["POST"])
def api():
    data: dict = request.get_json()
    url = upload.main(teletype_url=data['link'], name=data['name'], author_url=data['username'], boosty_auth=data.get("boosty_auth"))
    if url:
        return {"url": url}
    else:
        return 500

if __name__ == '__main__':
    host = f'127.0.100.100'

    # os.system(f'start chrome {host}')
    app.run(host=host, port=80)
    
    
    
    
    
    