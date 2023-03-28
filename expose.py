class Test()
    @cherrypy.expose
    def foo(self):
        return "Foo"
 
    def bar(self):
        return "Bar"
    bar.exposed=True

