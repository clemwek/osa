import MySQLdb

def  connection():
	conn = MySQLdb.connect(host = "localhost", user = "admin",
		passwd = "password", db = "osa")
	c = conn.cursor()

	return c, conn