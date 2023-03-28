import cherrypy

@cherrypy.expose
class NameWebService(object):
    string = ''

    def GET(self):
        return self.mystr
    
    @cherrypy.tools.accept(media='text/plain')
    def POST(self,*args):
        mystr = ''
        for i in args:
            mystr+=' '+str(i)
        self.mystr = mystr
        return mystr+" are given"

conf = {
    '/': {
    'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
    'tools.response_headers.on': True,
    'tools.response_headers.headers': [('Content-Type', 'text/plain')],
    }
}
cherrypy.quickstart(NameWebService(), '/', conf)


