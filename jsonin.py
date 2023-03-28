import cherrypy

class MyApp:
    @cherrypy.expose
    @cherrypy.tools.json_in()
    def index(self):
        return cherrypy.request.json.get('name')
    
cherrypy.quickstart(MyApp())


