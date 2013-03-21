from bottle import view, route, request, response
from model.model import *

@route("/")
@view("home")
def home():
	viewData = {}
	return viewData


@route("/api/ideas", method="GET")
def api_listIdeas():
	ideas = Idea.query.all()
	result = [idea.toDict() for idea in ideas]

	return result

@route("/api/idea", method="POST")
def api_newIdea():
	try:
		if "ideaName" not in request.all or len(request.all["ideaName"].strip()) < 4:
			raise Exception("You must provide a name for this hackathon idea!")

		if "description" not in request.all:
			raise Exception("You must pass in 'description'")

		if "enteredBy" not in request.all:
			raise Exception("You must pass in 'enteredBy'")

		#
		# Save our new idea
		#
		newIdea = Idea(
			ideaName = request.all["ideaName"],
			description = request.all["description"],
			enteredBy = request.all["enteredBy"]
		)

		session.commit()
		return newIdea.id

	except Exception as e:
		print e

		response.status = 500
		return e.message


@route("/api/idea/<id>", method="DELETE")
def api_removeIdea(id):
	Idea.get_by(id=id).delete()
	session.commit()
