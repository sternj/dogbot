from flask import Flask, send_file, render_template
import io
import nltk
import os
from dogs.captioner import caption
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/dog')
def send_dog():
    img = caption.put_text(True)
    img_recv = io.BytesIO()
    img.save(img_recv, "JPEG")
    img_recv.seek(0)
    return send_file(img_recv, mimetype='image/jpeg', as_attachment=False)

@app.before_first_request
def download_punkt():
    nltk.download('punkt')


# NOTE: derived from https://flask.palletsprojects.com/en/master/server/
if __name__ == "__main__":
    print(__file__)
    os.chdir('/home/sam/Projects/code/dogbot')
    app.run(debug=True)
