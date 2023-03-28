import cherrypy
class MyApp:
    @cherrypy.expose
    def index(self):
        return 'Hello Cherries'

    @cherrypy.expose
    def myname(self):
        return 'Ariharasudhan'

cherrypy.quickstart(MyApp())
    



