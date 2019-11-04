import http.server

class SERVER:
    def __init__(self):
        print()
        #PORT = 8000
        #Handler = http.server.SimpleHTTPRequestHandler
        #httpd = http.server.TCPServer(("", PORT), Handler)
        #http.server.BaseHTTPRequestHandler

    def run_while_true(self, server_class=http.server, handler_class=http.server.BaseHTTPRequestHandler):
        """
        This assumes that keep_running() is a function of no arguments which
        is tested initially and after each request.  If its return value
        is true, the server continues.
        """
        server_address = ('', 8080)
        httpd = server_class(server_address, handler_class)
        while self.keep_running():
            httpd.handle_request()

    def keep_running(self):
        return True