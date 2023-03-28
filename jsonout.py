import cherrypy

class MyApp:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        return {'name':'Ari'}
    
cherrypy.quickstart(MyApp())


