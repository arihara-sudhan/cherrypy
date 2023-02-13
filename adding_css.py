import cherrypy
import os 
class MyApp(object):
    @cherrypy.expose
    def index(self):
        return """<html><head>
    <link href="/static/css/styles.css" rel="stylesheet">
    </head>
    <h1>I am ARI</h1>"""

conf = {
   '/': {
     'tools.staticdir.root': os.path.abspath(os.getcwd())
     },
   '/static': {
       'tools.staticdir.on': True,
       'tools.staticdir.dir': './public'
     }
}
    
cherrypy.quickstart(MyApp(), '/', conf)



