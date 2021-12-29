from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='./build/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
######################
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
#########################

@app.route('/', defaults={"filename": "index.html"})
@app.route('/<path:filename>')
def index(filename):
    return send_from_directory('./build', filename)

@app.route('/api/test')
def endpoint_current_time():
    #Endpoint for Current Time.
    print("----------\nCurrent Time Endpoint Reached")
    return {'current_time': current_time}

app.run(
    host=os.getenv('IP',"0.0.0.0"),
    port=int(os.getenv("PORT",8081)),
    debug=True,
    )
