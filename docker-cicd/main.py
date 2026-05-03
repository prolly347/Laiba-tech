from http.server import HTTPServer, BaseHTTPRequestHandler

class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        html = b"""
        <html>
        <body style="text-align:center; padding:50px; font-family:Arial;">
            <h1>CI/CD Pipeline Successful</h1>
            <h2>Dockerized Application Running</h2>
            <p>GitHub Actions Deployment Lab</p>
        </body>
        </html>
        """

        self.wfile.write(html)

print("Server running on port 8080")
server = HTTPServer(('0.0.0.0', 8080), AppHandler)
server.serve_forever()
