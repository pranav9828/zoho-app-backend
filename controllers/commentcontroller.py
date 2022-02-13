from flask import json
import db
from datetime import datetime

class CommentController:    
    def createNewComment(self, userid, comment):
        uid = ''.join(userid)
        cm = ''.join(comment)
        mysql = db.configureDatabase()
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            currentDateTime = datetime.now()
            cursor.execute("INSERT INTO comments(userid,comment,createdat) VALUES (%s, %s, %s)", (uid, cm , currentDateTime))
            conn.commit()
            return ({"message": "Success",'status' : 200}) 
        except Exception as e:
            return json.dumps({'error':str(e)})   
        finally:
            cursor.close()
            conn.close()

    def getComments(self):
        mysql = db.configureDatabase()
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT users.id, users.email, comments.id, comments.comment, comments.createdat FROM users JOIN comments ON users.id = comments.userid ORDER BY comments.createdAt desc")
            comments_list = []
            comments = cursor.fetchall()
            for comment in comments:
                res = {}
                res.update({"user_id": comment[0], "email": comment[1], "comment_id": comment[2], "comment": comment[3], "created_at": comment[4]})
                comments_list.append(res)
            return comments_list
        except Exception as e:
            return json.dumps({'error':str(e)})   
        finally:
            cursor.close()
            conn.close()         