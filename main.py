from http.server import HTTPServer, CGIHTTPRequestHandler

server_data = ("localhost", 8000)
server = HTTPServer(server_data, CGIHTTPRequestHandler)
server.serve_forever()