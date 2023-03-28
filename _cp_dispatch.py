import cherrypy

class MyApp:
    def _cp_dispatch(self,vpath):
        if(len(vpath) == 1):
            cherrypy.request.params['name'] = vpath.pop()
            return self
        if(len(vpath) == 3):
            cherrypy.request.params['name'] = vpath.pop(0)
            cherrypy.request.params['color'] = vpath.pop(0)
            cherrypy.request.params['taste'] = vpath.pop(0)
            return Fruit()
    @cherrypy.expose
    def index(self,name):
        return 'This is %s'%name
    
class Fruit:
    @cherrypy.expose
    def index(self,name,color,taste):
        return 'This is %s which is %s in color and %s'%(name,color,taste)
    
cherrypy.quickstart(MyApp())