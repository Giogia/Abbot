from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import threading
import SimpleHTTPServer
import sys

PORT = 8080

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    server = ThreadedHTTPServer(('0.0.0.0', PORT), Handler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
