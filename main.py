from flask import Flask, request, render_template
import upload
import os
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home():
    url = ''
    if request.method == 'POST':
        files = request.files.getlist('files')
        url = upload.main(images=files, title=request.form['title'], name=request.form['name'], author_url=request.form['telegram_url'])
    return render_template('index.html', url=url)


if __name__ == '__main__':
    domen = 'khudoberdi.aziz'
    host = f'127.0.100.100 {domen}'

    with open(r'c:\windows\system32\drivers\etc\HOSTS', 'r', encoding='utf-8') as f:
        isHost = False
        for i in f.readlines():
            if i.strip() == host:
                isHost = True
        if not isHost:
            os.system(f"echo {host} >> c:\windows\system32\drivers\etc\HOSTS")

    os.system(f'start chrome {domen}')
    app.run(host=domen, port=80)
    
    
    
    
    
    