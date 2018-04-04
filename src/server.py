from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from cowpy import cow
import json

default = cow.Satanic(thoughts=True)


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """HTTP handler."""
    def do_GET(self):
        """Routing for GET requests."""
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == '/':
            print(self.headers)
            self.send_response(200)
            self.end_headers()

            self.wfile.write(b'<a href="/cowsay">Cowsay</a>')
            return

        elif parsed_path.path == '/cowsay':
            msg = default.milk('Go to 127.0.0.1/cow?msg=<your message here> to make a cow talk!')

            self.send_response(200)
            self.end_headers()
            self.wfile.write(msg.encode('utf8'))
            return

        elif parsed_path.path == '/cow':
            try:
                text = parsed_qs['msg'][0]
                msg = default.milk(text)

                self.send_response(200)
                self.end_headers()
                self.wfile.write(msg.encode('utf8'))
                return

            except KeyError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'Ya dun goofed in a GET!')
                return

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'This doesn\'t exist in GET!')

    def do_POST(self):
        """Routing for POST requests."""
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == '/cow':
            try:
                self.send_response(200)
                self.end_headers()
                text = parsed_qs['msg'][0]
                msg = json.dumps(default.milk(text))
                self.wfile.write(msg.encode('utf8'))
                return

            except KeyError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'Ya dun goofed in a POST!')
                return
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'This doesn\'t exist in POST!')


def create_server():
    """Instantiate an HTTP server."""
    return HTTPServer(('127.0.0.1', 3000), SimpleHTTPRequestHandler)


def run_forever():
    """Keep the server running."""
    server = create_server()

    try:
        print('Starting server on port 3000')
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()


if __name__ == '__main__':
    run_forever()
