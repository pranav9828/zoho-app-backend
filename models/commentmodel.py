from calendar import c
from flask import jsonify
from flask import json
from controllers import commentcontroller

class Comment:
    def __init__(self, comments, userid):
        self.comments = comments,
        self.userid = userid,    

    def createComment(self):
        userid = ''.join(self.userid)
        comment = ''.join(self.comments)
        if userid is None or userid == '':
            return ({'error': 'User Id is required', 'status' : 400})
        elif comment is None or comment == '':
            return ({'error': 'Comment is required', 'status' : 400})
        else:
            cController = commentcontroller.CommentController()
            response = cController.createNewComment(userid, comment)
            response = jsonify(response);
            return response

    def getAllComments(self):
        cController = commentcontroller.CommentController()
        response = cController.getComments()
        response = jsonify(response);
        return response