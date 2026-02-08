#!/usr/bin/env python3
"""
Simple HTTP server for Effective Mobile test task
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import socket

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            response = b"Hello from Effective Mobile!"
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.send_header('Content-Length', str(len(response)))
            self.end_headers()
            self.wfile.write(response)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

    def log_message(self, format, *args):
        # Disable default logging
        pass

def run_server():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    # Get container hostname for logging
    hostname = socket.gethostname()
    print(f"Starting backend server on port 8080 (hostname: {hostname})")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.server_close()

if __name__ == '__main__':
    run_server()
