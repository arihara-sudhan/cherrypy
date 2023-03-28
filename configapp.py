import cherrypy

class MyApp:
    @cherrypy.expose
    def index(self):
        return cherrypy.request.json.get('name')
    index._cp_config = {'tools.json_in': True}


cherrypy.quickstart(MyApp())


