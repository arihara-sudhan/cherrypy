import cherrypy
class MyApp:
    @cherrypy.expose
    def index(self):
        return 'Hello Cherries'

cherrypy.quickstart(MyApp())
    



