import config 
import datetime

from elixir import *

metadata.bind = config.DB_CONNECTION_STRING
metadata.bind.echo = True

class Idea(Entity):
	using_options(tablename="idea")

	ideaName = Field(Unicode(50), nullable=False)
	description = Field(Text(), nullable=True)
	enteredBy = Field(Unicode(50), nullable=True)

	def toDict(self):
		return {
			"id": self.id,
			"ideaName": self.ideaName,
			"description": self.description,
			"enteredBy": self.enteredBy
		}

	def __repr__(self):
		return "<Idea \"%s\" (%s)>" % (self.ideaName, self.id)
