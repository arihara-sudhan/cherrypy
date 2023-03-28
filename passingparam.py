import cherrypy
class MyApp:
    @cherrypy.expose
    def myage(self,age=20):
        return "You are "+str(age)+" years old!"

cherrypy.quickstart(MyApp())
    



