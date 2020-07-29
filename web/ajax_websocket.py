
##################################################################################################

import datetime
import time

from flask import Flask, render_template, request

##################################################################################################

app = Flask('TEST WEBPAGE',
            static_folder = 'static',
            template_folder = 'templates')

app.config.from_object('security')

@app.route("/ajax")
def ajax():
    return render_template("ajax.jinja")

@app.route("/send")
def hello():
    #request.args['data']
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')




app.run(host="0.0.0.0", port=7777, debug = True)
