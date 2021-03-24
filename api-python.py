import flask
import requests
import json

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
		comments.insert((author, messagebody))
		return flask.jsonify(createjsonerror("200", "Successfully commented.")), 200
	else:
		return flask.jsonify(createjsonerror("message must be less than 50 characters", "Message length exeded.")), 500
	return flask.jsonify(createjsonerror("something went wrong", "Something went wrong.")), 500

@app.route('/comments/get/<numtoget>')
def getcomments(numtoget)
	response = []
	x = 0
	for i in range(0, numtoget, 1):
		try:
			response.append(comments[x])
		except:
			break
		x += 1
		return flask.jsonify(json.dump(response)), 200
	
app.run()
	
