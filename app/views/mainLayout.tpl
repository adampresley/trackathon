<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<title>{{title}} // Trackathon</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<meta name="description" content="An application for groups or organizations to track and manage Hackathons" />
	<meta name="author" content="Adam Presley" />
	<meta name="Content-Language" content="en" />

	<!--CSS-START-->
	<link href="http://fonts.googleapis.com/css?family=PT+Sans:400,400italic,700,700italic&amp;subset=latin,latin-ext" rel="stylesheet" type="text/css" />
	<link href="/resources/css/bootstrap.css" rel="stylesheet" />
	<link href="/resources/css/bootstrap2.css" rel="stylesheet" />
	<link href="/resources/css/style.css" rel="stylesheet" />
	<link href="/resources/css/font-awesome.css" rel="stylesheet" />
	<!--CSS-END-->

	<!--[if lt IE 9]>
	<script src="/resources/js/html5.js"></script>
	<![endif]-->
</head>

<body>
	<header>
		<div class="container">
			<div class="row">
				<div class="span12">
					<div id="logo">
						Trackathon
					</div>

					<div id="mainNavContainer">
						<ul id="mainNav">
							<li class="home">
								<a href="/" class="btn btn-warning"><i class="icon-home"></i> <span>Home</span></a>
							</li>
							
							<li class="features dropdown">
								<a href="#" class="btn btn-warning dropdown-toggle" data-toggle="dropdown"><i class="icon-pencil"></i> <span>Ideas</span><b class="caret"></b></a>
								<ul class="dropdown-menu">
									<li><a href="#" id="suggest" data-bind="click: goToPage"><i class="icon-plus-sign icon-white"></i> Suggest a Hackathon</a></li>
								</ul>
							</li>
						</ul>
					</div><!-- mainNavContainer -->
				</div>
			</div>
		</div>
	</header>

	<div class="container-fluid">
		<div class="row-fluid">
			<div class="span12">
				<!--JS-START-->
				<script src="/resources/js/jquery.js"></script>
				<script src="/resources/js/jquery.blockui.js"></script>
				<script src="/resources/js/bootstrap.js"></script>
				<script src="/resources/js/knockout.js"></script>
				<script src="/resources/js/sammy.js"></script>
				<script src="/resources/js/trackathon.js"></script>
				<!--JS-END-->
				
				<!-- CONTENT -->
				<div class="row-fluid">
					<div class="span12" id="contentContainer">
						%include
					</div>
				</div>
				<!-- END-CONTENT -->
			</div><!--/span-->
		</div><!--/row-->

		<hr>

		<footer>
			<p>&copy; Adam Presley 2013</p>
		</footer>
	</div><!--/.fluid-container-->
</body>
</html>