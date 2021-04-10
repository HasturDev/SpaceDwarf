from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return {"body":"hello, world!"}

@app.route('/somethingdarkside')
def darkside():
    return "something, something, something, darkside."

