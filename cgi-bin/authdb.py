import database_manager
import cgi, cgitb
cgitb.enable()		## allows for debugging errors from the cgi scripts in the browser

form = cgi.FieldStorage()

## getting the data from the fields
organization = form.getvalue('organization')
first_name = form.getvalue('username')
last_name = form.getvalue('password')

html = """
    <html>
    <head><title>User %s</title></head>
    <body>
    <h1>%s</h1>
    <b>Organization : </b> %s <br>
    <b>Firstname : </b> %s <br>
    <b>Lastname : </b> %s <br>
    </div>
    </body>
    </html>
    """

authdb = database_manager.MANAGER()
result = authdb.findUser(organization, first_name, last_name)
if(result != None):
    print("Content-type:text/html\r\n\r\n")
    print(html % ("Does Exists", "User has successfully logged in", organization, first_name, last_name))
else:
    print("Content-type:text/html\r\n\r\n")
    print(html % ("Does Not Exist", "User does not exist, Debug only (normal Drop)", organization, first_name, last_name))