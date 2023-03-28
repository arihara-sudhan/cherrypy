import cherrypy
class MyApp(object):
    @cherrypy.expose
    def index(self):
        return """<html>
            <head></head>
            <body>
                <form method="get" action="myname">
                    <input type="text" name="name" />
                    <button type="submit">DONE</button>
                </form>
            </body>
        </html>"""
    
    @cherrypy.expose
    def myname(self, name='Ari'):
        cherrypy.session['urnamesession'] = name
        urname = "Your name is "+name
        return urname
            
    @cherrypy.expose
    def display(self):
        return cherrypy.session['urnamesession']

conf = { '/': { 'tools.sessions.on': True } }
cherrypy.quickstart(MyApp(), '/', conf)



