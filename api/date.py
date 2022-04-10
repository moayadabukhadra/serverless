from http.server import BaseHTTPRequestHandler , HTTPServer


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    #  request is successful and you will get your response
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(self.path[1:].encode())
    return

# def main():
#     PORT=3000
#     server= HTTPServer(('',PORT),handler)
#     print('%s'% PORT)
#     server.serve_forever()

# if __name__=='__main__':
#     main()
