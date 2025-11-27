from flask import Flask, render_template, request
import qrcode
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    link = request.form['link']

    img = qrcode.make(link)
    img_path = "static/qr.png"
    img.save(img_path)

    return render_template('index.html', qr_image=img_path)

if __name__ == "__main__":
    app.run(debug=True)
