import email
from urllib import request
from flask import Flask, request, jsonify
from models import usermodel
from models import commentmodel

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h2>Welcome to Zoho App!</h2>'

@app.route('/api/v1/user', methods=['POST'])
def createUser():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']
        code = request.form['secretcode']
        user = usermodel.User(email=email, password=pwd, secret_code=code)
        res = user.createNewUser();
        return res

@app.route('/api/v1/login', methods=['POST'])
def loginUser():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']
        user = usermodel.User(email=email, password=pwd, secret_code='')
        res = user.login();
        return res

@app.route('/api/v1/forgotpassword', methods=['POST'])
def getPassword():
    if request.method == 'POST':
        email = request.form['email']
        code = request.form['secretcode']
        user = usermodel.User(email=email, password='', secret_code=code)
        res = user.forgotPassword();
        return res   

@app.route('/api/v1/comment', methods=['POST', 'GET'])
def comments():
    if request.method == 'POST':
        userid = request.form['userid']
        comments = request.form['comments']
        cmodel = commentmodel.Comment(comments=comments, userid=userid)
        res = cmodel.createComment();
        return res 
    elif request.method == 'GET':
        cmodel = commentmodel.Comment(comments='', userid='')
        res = cmodel.getAllComments();
        return res 


if __name__ == '__main__':
    app.run(debug=True)