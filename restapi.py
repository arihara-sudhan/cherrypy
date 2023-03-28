import cherrypy

@cherrypy.expose
class NameWebService(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return cherrypy.session['mystring']

    def POST(self):
        some_string = "ARIHARASUDHAN"
        cherrypy.session['mystring'] = some_string
        return some_string

    def PUT(self, another_string):
        cherrypy.session['mystring'] = another_string

    def DELETE(self):
        cherrypy.session.pop('mystring', None)

conf = {
    '/': {
    'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
    'tools.sessions.on': True,
    'tools.response_headers.on': True,
    'tools.response_headers.headers': [('Content-Type', 'text/plain')],
    }
}
cherrypy.quickstart(NameWebService(), '/', conf)