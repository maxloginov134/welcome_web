from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPost = 8080


class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes('Hello, World wide web!', "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPost), Server)
    print("Server started http://%s:%s" % (hostName, serverPost))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped")
