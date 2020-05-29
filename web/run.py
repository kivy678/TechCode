# -*- coding:utf-8 -*-

##################################################################################################
import os

from flask import Flask, render_template, request
from flask import send_from_directory
from werkzeug.utils import secure_filename

from tornado.wsgi       import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop     import IOLoop

from FruitViwer import FruitViwer

##################################################################################################

app = Flask('TEST WEBPAGE',
            static_folder = 'static',
            template_folder = 'templates')

app.config.from_object('security')

##################################################################################################

@app.route("/downloads", methods = ['GET'])
def downloads():
    return send_from_directory(directory="DirectoryPath", filename="FileName", as_attachment=True)

@app.route("/uploads", methods = ['POST'])
def uploads():
    if request.method == 'POST':
        f = request.files['file']
        option = request.form['option']

        f.save(os.path.join("DirectoryPath", secure_filename(f.filename)))

    return "OK"

viwer = FruitViwer.as_view('/view', template_name='view.jinja')
app.add_url_rule('/view', view_func=viwer, methods=['GET'])


from blueprint import setup as BaseSetup
BaseSetup(app)


@app.route("/")
def index():
    return render_template("index.jinja")


def getServer(port):
    server = HTTPServer(WSGIContainer(app))
    server.listen(port)
    return IOLoop.instance()


if __name__ == '__main__':
    # Flask running
    app.run(host="0.0.0.0", port=5555, debug = True)
    
    # tornadorunning
    #server = getServer(5555)
    #server.start()

    print("Main done...")
