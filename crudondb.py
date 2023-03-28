import random
import sqlite3
import string
import time
import cherrypy
DB_STRING = "my.db"

@cherrypy.expose
class NameService(object):
    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        with sqlite3.connect(DB_STRING) as c:
            r = c.execute("SELECT * FROM ranstrs")
        return r.fetchone()

    def POST(self):
        some_string = ''.join(random.sample(string.hexdigits,8))
        with sqlite3.connect(DB_STRING) as c:
            c.execute("INSERT INTO ranstrs VALUES (?)",[some_string])
        return "INSERTED A RANDOM STRING"

    def PUT(self, another_string):
        with sqlite3.connect(DB_STRING) as c:
            c.execute("UPDATE ranstrs SET value=?",[another_string])
        return "UPDATED ALL ROWS"
    
    def DELETE(self):
        with sqlite3.connect(DB_STRING) as c:
            c.execute("DELETE * FROM ranstrs")
        return "DELETED ALL ROWS"
    
def setup_database():
    with sqlite3.connect(DB_STRING) as con:
        con.execute("CREATE TABLE ranstrs (value)")

def cleanup_database():
    with sqlite3.connect(DB_STRING) as con:
        con.execute("DROP TABLE ranstrs")

conf = {
    '/': {
    'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
    'tools.response_headers.on': True,
    'tools.response_headers.headers': [('Content-Type', 'text/plain')],
    }
}
cherrypy.engine.subscribe('start', setup_database)
cherrypy.engine.subscribe('stop', cleanup_database)
cherrypy.quickstart(NameService(), '/', conf)


