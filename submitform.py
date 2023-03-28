import cherrypy

class MyApp:
    @cherrypy.expose
    def index(self):
        return """<html>
                    <head></head>
                        <body>
                            <form method="get" action="myage">
                                <input type="number" placeholder="Age" name="age" />
                                <button type="submit">DONE</button>
                            </form>
                        </body>
                </html>"""
    
    @cherrypy.expose
    def myage(self,age=20):
        return "Your are "+str(age)+" years old"
        
                
cherrypy.quickstart(MyApp())



