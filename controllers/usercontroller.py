from flask import json
import db

class UserController:    
    def userSignUp(self, email, password, secretcode):
        em = ''.join(email)
        pwd = ''.join(password)
        code = ''.join(secretcode)
        mysql = db.configureDatabase()
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            if(self.checkUser(email)):
                return ({"error": "Email already exists", 'status' : 400})
            else:
                cursor.execute("INSERT INTO users(email,password,secretcode,islogin) VALUES (%s, %s, %s,%s)", (em, pwd , code, "1"))
                conn.commit()
                return ({"message": "Success",'status' : 200})
        except Exception as e:
            return json.dumps({'error':str(e)})   
        finally:
            cursor.close()
            conn.close()

    def userLogin(self, email, password):
        em = ''.join(email)
        pwd = ''.join(password)
        mysql = db.configureDatabase()
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            if(self.checkUser(email)):
                mysql = db.configureDatabase()
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (em, pwd))
                conn.commit()
                info = cursor.fetchall()
                print(info)
                if len(info) > 0:
                    res = {}
                    user_id = 0;
                    for data in info:
                        user_id = data[0]
                        res.update({"id": data[0], "email": data[1], "secretcode": data[3], "islogin": data[4], "message": "Success", "status": 200})
                    return res
                else:
                    return {"error": "Incorrect Email ID or Password", "status": 400}
            else:
                return {"error": "User does not exist", "status": 400}

        except Exception as e:
            return json.dumps({'error':str(e)})   
        finally:
            cursor.close()
            conn.close()

    def userForgotPassword(self, email, code):
        em = ''.join(email)
        secretcode = ''.join(code)
        mysql = db.configureDatabase()
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            if(self.checkUser(email)):
                mysql = db.configureDatabase()
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute("SELECT password FROM users WHERE email = %s AND secretcode = %s", (em, secretcode))
                conn.commit()
                info = cursor.fetchall()
                print(info)
                if len(info) > 0:
                    pwd = ''.join(info[0])
                    return {"password": pwd, "status": 200}
                else:
                    return {"error": "Incorrect secret code", "status": 400}
            else:
                return {"error": "User does not exist", "status": 400}

        except Exception as e:
            return json.dumps({'error':str(e)})   
        finally:
            cursor.close()
            conn.close()                

    def checkUser(self, email):
        mysql = db.configureDatabase()
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM users WHERE email = %s", (email))
            data = cursor.fetchall()
            if len(data) > 0:
                conn.commit()
                return True
            
        except Exception as e:
            return False
        
        finally:
            cursor.close()
            conn.close()