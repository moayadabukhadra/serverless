from http.server import BaseHTTPRequestHandler , HTTPServer
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    #  request is successful and you will get your response
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    r = requests.get('https://serverless-virid-eight.vercel.app/')
    r.status_code
    r.headers['content-type']
    self.wfile.write(r.headers['content-type'].encode())

