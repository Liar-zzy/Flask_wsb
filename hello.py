from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from flask import jsonify
from pypinyin import lazy_pinyin
from flask import send_from_directory
from flask import session

import time
import os
from werkzeug.utils import secure_filename
from dealExcel import *


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload/'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/*')
def none():
    return 404


@app.route('/refresh')
def refresh():
    kind = request.args.get('kind')
    # print(kind)

    return "none"


@app.route('/upload')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']

        # f.save(os.path.join(
        #     app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        file_name = secure_filename(''.join(lazy_pinyin(f.filename)))
        f.save(os.path.join(
            app.config['UPLOAD_FOLDER'], file_name))

        output = dealExcel(file_name)
        print(output)
        session['filename'] = output

        # as_attachment=True 一定要写，不然会变成打开，而不是下载
        return redirect(url_for('downloader'))


@app.route("/download")
def downloader():
    file_name = session.get('filename')
    print(file_name)
    print("download")
    dirpath = os.path.join(app.root_path, 'output')
    print(dirpath)
    return send_from_directory(dirpath, file_name, as_attachment=True)


if __name__ == '__main__':
    app.run()
