import http.server
import socketserver

PORT = 8080

# Create a request handler
Handler = http.server.SimpleHTTPRequestHandler

# Create and configure the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
