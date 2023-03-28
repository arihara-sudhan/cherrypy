from cherrypy.lib.static import serve_file
import cherrypy
import os 

class MyApp:
    @cherrypy.expose
    def index(self):
        return '''
            <form method="GET" action="download">
                <input type='submit' value="Download">
            </form>
        '''
    @cherrypy.expose
    def download(self):
        return serve_file(os.path.abspath("files/myfile.txt"), "application/x-download", "attachment")

cherrypy.quickstart(MyApp())
