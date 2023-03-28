import cherrypy

class MyApp:
	@cherrypy.expose
	def index(self):
		return """<html>
            <body>
            	<form action ="store" method ="GET">
                	<input type ="file" name ="myFile" /><br />
            	    <input type ="submit" /></div>
            	</form>            			
            </body>
            </html>
            """
	@cherrypy.expose
    def read(self):
        return
        
cherrypy.quickstart(MyApp())
