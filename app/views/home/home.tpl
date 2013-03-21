<p data-bind="visible: ideas().length <= 0">No ideas submitted yet. Submit one now!</p>

<table id="ideasTable" class="table table-striped" data-bind="visible: ideas().length > 0">
	<thead>
		<tr>
			<th style="width: 1%;">&nbsp;</th>
			<th>Idea Name</th>
			<th>Description</th>
			<th>Entered By</th>
		</tr>
	</thead>
	<tbody data-bind="foreach: ideas">
		<tr>
			<td><button class="button" class="btn" data-bind="click: $root.removeIdea"><i class="icon-remove-circle icon-white"></i></button></td>
			<td data-bind="text: ideaName"></td>
			<td data-bind="text: description"></td>
			<td data-bind="text: enteredBy"></td>
		</tr>
	</tbody>
</table>

<div id="newIdeaModal" class="modal hide fade" role="dialog" aria-hidden="true">
	<div class="modal-header">
		<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
		<h3>Suggest a Hackathon</h3>
	</div>

	<div class="modal-body">
		<label for="newIdeaName">Idea Name</label>
		<input type="text" id="newIdeaName" maxlength="50" class="span8" />

		<label for="newEnteredBy">Entered By</label>
		<input type="text" id="newEnteredBy" maxlength="50" class="span6" />

		<label for="newDescription">Describe Your Idea</label>
		<textarea id="newDescription" rows="5" class="span10"></textarea>
	</div>

	<div class="modal-footer">
		<a href="#" class="btn btn-error" data-bind="event: {click: cancelNewIdea}">Cancel</a>
		<a href="#" class="btn btn-primary" data-bind="event: {click: saveNewIdea}">Save</a>
	</div>
</div>

<script>
	ko.applyBindings(new Trackathon.ViewModel.Index());
</script>

% rebase mainLayout title="Home"