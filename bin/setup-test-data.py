import os, sys

sys.path.insert(0, "../")

from elixir import *
from config import *
from model.model import *

setup_all()

#
# Create some ideas
#
idea1 = Idea(ideaName="First Idea", description="This is the first idea for a hackathon. We wanna build stuff that rocks!", enteredBy="Adam Presley")
idea2 = Idea(ideaName="Second Idea", description="This is the second idea for a hackathon. We wanna build stuff that rocks even more!", enteredBy="Mark DeMoss")

session.commit()
