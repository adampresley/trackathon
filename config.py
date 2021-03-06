import os

DEBUG = True
BIND_TO_OUTSIDE_IP = False
BIND_TO_PORT = 8000

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
APP_PATH = os.path.join(ROOT_PATH, "app")
RESOURCES_PATH = os.path.join(APP_PATH, "resources")
BASE_TEMPLATE_PATH = os.path.join(APP_PATH, "views")
SESSION_PATH = os.path.join(APP_PATH, "sessions")


ENV = "dev"

ENVIRONMENTS = {
	"dev": {
		"DBSERVER": "localhost",
		"DBUSER": "user",
		"DBPASS": "password"
	},
	"test": {
		"DBSERVER": "localhost",
		"DBUSER": "user",
		"DBPASS": "password"
	},
	"beta": {
		"DBSERVER": "localhost",
		"DBUSER": "user",
		"DBPASS": "password"
	},
	"demo": {
		"DBSERVER": "localhost",
		"DBUSER": "user",
		"DBPASS": "password"
	},
	"prod": {
		"DBSERVER": "localhost",
		"DBUSER": "user",
		"DBPASS": "password"
	},
}

DBNAME = "trackathon"
DBSERVER = ENVIRONMENTS[ENV]["DBSERVER"]
DBUSER = ENVIRONMENTS[ENV]["DBUSER"]
DBPASS = ENVIRONMENTS[ENV]["DBPASS"]

#
# Specify your database connection string here. Need more
# info on connection strings? Visit
# http://docs.sqlalchemy.org/en/rel_0_7/dialects/
#
DB_CONNECTION_STRING = "sqlite:///%s/%s.db" % (ROOT_PATH, DBNAME)


#
# Session settings
#
SESSION_OPTS = {
	"session.type": "ext:database",
	"session.cookie_expires": 14400,
	"session.auto": True,
	"session.url": DB_CONNECTION_STRING,
	"session.table_name": "admin_session",
	"session.lock_dir": os.path.join(SESSION_PATH, "lock"),
	"session.data_dir": os.path.join(SESSION_PATH, "data")
}
