#!/usr/bin/env python3

import SimpleHTTPServer
import SocketServer

PORT = 8002

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()