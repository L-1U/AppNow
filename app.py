from flask import Flask
from flask import request
from github import Github

port = sys.argv[1]
app = Flask(__name__)

@app.route('/hellow')
def hello_world():
    from jwt import (
    JWT,
    jwk_from_pem,
)
    return 'Hello, World!'

@app.route('/img')
def callimg():
    from img import show
    s = "img"+show()
    return s

@app.route('/github', methods = ['POST'])
def github():
    content = request.get_json()
    action = content["action"]
    if action=="edited":
        appid = content["installation"]["id"]
        from GetKey import genToken
        st = genToken(appid)
        print("TOKEN = "+st)
    return st

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port)