import cherrypy
class MyApp:
    @cherrypy.expose
    def index(self):
       cherrypy.log("Hello There")

cherrypy.tree.mount(MyApp(),'/mine')
cherrypy.engine.start()
cherrypy.engine.block()


