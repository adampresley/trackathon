Trackathon = {
	"Dialog": {},
	"Model": {},
	"Util": {},
	"ViewModel": {},
};

Trackathon.Util.block = function(message, el) {
	if (el) {
		$(el).block({ message: "<h3 style='padding-top: 6px;'>" + message + "</h3>" });
	} else {
		$.blockUI({ message: "<h3 style='padding-top: 6px;'>" + message + "</h3>" });
	}
};

Trackathon.Util.unblock = function(el) {
	if (el) {
		$(el).unblock();
	} else {
		$.unblockUI();
	}
};

Trackathon.Model.Idea = function(id, ideaName, description, enteredBy) {
	var self = this;

	self.id = id || 0;
	self.ideaName = ideaName || "";
	self.description = description || "";
	self.enteredBy = enteredBy || "";
};

Trackathon.Model.IdeaService = function() {
	var self = this;

	self.list = function(callback) {
		$.get("/api/ideas").done(function(data) {
			var mappedIdeas = $.map(data, function(item) { 
				return new Trackathon.Model.Idea(item.id, item.ideaName, item.description, item.enteredBy);
			});

			callback(mappedIdeas);
		});
	};

	self.save = function(idea, callback) {
		var data = {
			ideaName: idea.ideaName,
			description: idea.description,
			enteredBy: idea.enteredBy
		};

		$.post("/api/idea", data).done(function(result) {
			Trackathon.Util.unblock();
			callback(data);
		}).fail(function(result) {
			Trackathon.Util.unblock();
			alert("Uh oh, something went wrong!");
		});
	};

	self.remove = function(idea) {
		$.ajax({
			url: "/api/idea/" + idea.id, 
			method: "DELETE"
		});
	};
};


Trackathon.Dialog.NewIdea = function() {
	var self = this;

	self.service = new Trackathon.Model.IdeaService();
	
	/*
	 * The modal
	 */
	self._modal = $("#newIdeaModal");
	self._modal.modal({
		show: false
	});
	self._modal.on("shown", function() { $("#newIdeaName").focus(); });

	/*
	 * Elements
	 */
	self.$ideaName = $("#newIdeaName");
	self.$description = $("#newDescription");
	self.$enteredBy = $("#newEnteredBy");

	/*
	 * Methods
	 */
	self.show = function() {
		self._modal.modal("show");
	};

	self.close = function() {
		self._modal.modal("hide");
	};

	self.save = function(callback) {
		var idea = {};

		self.close();
		Trackathon.Util.block("Saving your new idea...");

		idea = new Trackathon.Model.Idea(0, self.$ideaName.val(), self.$description.val(), self.$enteredBy.val());
		console.log("save: %o", idea);
		self.service.save(idea, callback);

		self.$ideaName.val("");
		self.$description.val("");
	};
};


Trackathon.ViewModel.Index = function() {
	var self = this;

	self.chosenFolderId = ko.observable();
	self.ideas = ko.observableArray();
	self.newIdeaModal = new Trackathon.Dialog.NewIdea();
	self.ideaService = new Trackathon.Model.IdeaService();

	/*
	 * Load initial data
	 */
	self.ideaService.list(function(data) {
		var 
			length = data.length,
			i = 0;

		for (; i < length; i++) {
			self.ideas.push(data[i]);
		}
	});


	self.goToPage = function(data, e) { 
		self.chosenFolderId(e.target.id);

		if (e.target.id === "suggest") {
			self.newIdeaModal.show(); 
		}
	};

	self.cancelNewIdea = function() {
		self.newIdeaModal.close();
	};

	self.saveNewIdea = function() {
		self.newIdeaModal.save(function(data) {
			self.ideas.push(data);
		});
	};

	self.removeIdea = function(idea) {
		self.ideaService.remove(idea);
		self.ideas.remove(idea);
	};
}