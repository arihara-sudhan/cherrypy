import cherrypy
class MyApp:
    @cherrypy.expose
    def index(self):
        return "MINE"

class YourApp:
    @cherrypy.expose
    def index(self):
        return "YOURS"

cherrypy.tree.mount(MyApp(),'/mine')
cherrypy.tree.mount(YourApp(),'/yours')

cherrypy.engine.start()
cherrypy.engine.block()


