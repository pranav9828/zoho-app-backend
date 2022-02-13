from flask import jsonify
from flask import json
from controllers import usercontroller

class User:
    def __init__(self, email, password, secret_code):
        self.email = email,
        self.password = password,
        self.secretcode = secret_code,
    
    def createNewUser(self):
        email = ''.join(self.email)
        password = ''.join(self.password)
        code = ''.join(self.secretcode)

        if email is None or email == '':
            return ({'error': 'Email is required', 'status' : 400})
        elif password is None or password == '':
            return ({'error': 'Password is required', 'status' : 400})
        elif code is None or code == '':
            return ({'error': 'Secret code is required', 'status' : 400})
        else:
            ucontroller = usercontroller.UserController()
            response = ucontroller.userSignUp(email, password,code)
            response = jsonify(response);
            return response

    def login(self):
        email = ''.join(self.email)
        password = ''.join(self.password)
        if email is None or email == '':
            return ({'error': 'Email is required', 'status' : 400})
        elif password is None or password == '':
            return ({'error': 'Password is required', 'status' : 400})
        else:
            ucontroller = usercontroller.UserController()
            response = ucontroller.userLogin(email, password)
            response = jsonify(response);
            return response

    def forgotPassword(self):
        email = ''.join(self.email)
        code = ''.join(self.secretcode)
        if email is None or email == '':
            return ({'error': 'Email is required', 'status' : 400})
        elif code is None or code == '':
            return ({'error': 'Secret code is required', 'status' : 400})
        else:
            ucontroller = usercontroller.UserController()
            response = ucontroller.userForgotPassword(email, code)
            response = jsonify(response);
            return response        
