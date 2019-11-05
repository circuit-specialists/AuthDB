import sys
sys.path.append(".")
import database_manager
import cgi, cgitb
#cgitb.enable()		## allows for debugging errors from the cgi scripts in the browser

## security features needed
# set cookie
# test javascript
# after 5x attempts in 5min, ban for 30 min

form = cgi.FieldStorage()

## getting the data from the fields
organization = form.getvalue('organization')
first_name = form.getvalue('firstname')
last_name = form.getvalue('lastname')
password = form.getvalue('password')

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
result = authdb.authUser(organization, first_name, last_name, password)
if(result == None):
    print("Content-type:text/html\r\n\r\n")
    print(html % ("Does Not Exist", "User does not exist, Debug only (normal Drop)", organization, first_name, last_name))
elif(result):
    print("Content-type:text/html\r\n\r\n")
    print(html % ("Success", "User has successfully logged in", organization, first_name, last_name))
elif(not result):
    print("Content-type:text/html\r\n\r\n")
    print(html % ("Failed", "User has failed to log in", organization, first_name, last_name))
    