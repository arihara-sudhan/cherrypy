import cherrypy

class MyApp:
    @cherrypy.expose
    def index(self):
        return '''
            <form action=store method=GET>
                <input type='file' name='myFile'><br>
                <input type='submit'>
            </form>
    '''
    @cherrypy.expose
    def store(self,myFile):
        with open(myFile) as f:
            content = f.read()
        return content

cherrypy.quickstart(MyApp())



