import flask
import requests

comments = []

app = flask.Flask(__name__)
error = requests.get("https://static.cdn.ancoder.ml/404.html").content
def createjsonerror(message, usermessage):
	response = {"message":message, "usermessage":usermessage}
	return response

@app.errorhandler(404)
def pagenotfound():
	return error, 404

@app.route('/comments/create', methods = ['GET'])
def addcomment():
	author = flask.request.args.get("author")
	messagebody = flask.request.args.get("messagebody")
	if len(messagebody) < 50:
		comments.append((author, messagebody))
	else:
		return flask.jsonify(createjsonerror("message must be less than 50 characters", "Message length exeded")), 500
