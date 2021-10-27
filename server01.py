import os
from numpy import seterrobj
import last01
from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = os.urandom(12)


@app.route('/')
def index():
    return redirect(url_for('home'))


@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        blob_file = request.files.get('audio_file')
        last01.saveBlob(blob_file)
    return render_template('index.html')


@app.route('/result')
def result():
    return render_template('resultPage.html', result=last01.songRecognition())


# @app.route('/test', methods=['POST', 'GET'])
# def test():
#     if request.method == 'POST':
#         data = request.files.get('audio_file')
#         last01.testSaving(data)
#     return render_template('recording.html')


if __name__ == '__main__':
    app.run(debug=True)