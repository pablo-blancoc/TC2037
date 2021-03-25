from flask import Flask, request, url_for, redirect, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os
from automata import lexerAritmetico


UPLOAD_FOLDER = './static/files'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dfa', methods=['GET', 'POST'])
def dfa():
    # Página del autómata finito deterministico
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename('archivo.txt')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Mandar a llamar el procesamiento del archivo
            lexerAritmetico()   
            return redirect("static/files/result.txt")
    return render_template('dfa.html')


if __name__ == '__main__':
    app.run(debug=False)

