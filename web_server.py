import http.server
import time
import sys


class SERVER:
    def __init__(self):
        print("Starting Up HTTP Server...")
        self.address = ""
        self.port = 8080
        self.startServer()

    def startServer(self):
        handler = self.cgiHTTP()
        httpd = http.server.ThreadingHTTPServer(
            (self.address, self.port), handler)
        self.start_time = time.time()
        while self.keep_running():
            httpd.handle_request()

    def cgiHTTP(self):
        handler = http.server.CGIHTTPRequestHandler
        handler.cgi_directories = ["cgi-bin"]
        ## security features needed
        # set cookie
        # test javascript
        # after 5x attempts in 5min, ban for 30 min
        return handler

    def basicHTTP(self):
        handler = http.server.BaseHTTPRequestHandler ## requires implementation

    def simpleHTTP(self):
        return http.server.SimpleHTTPRequestHandler  # handles headers and GET

    def keep_running(self):
        if(time.time() < self.start_time + 30):
            return True
        else:
            return False
