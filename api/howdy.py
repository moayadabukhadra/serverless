from http.server import BaseHTTPRequestHandler , HTTPServer
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
   
    url = "https://catfact.ninja/fact"

    querystring = {"s":"Avengers Endgame","r":"json","page":"1"}

   

    response = requests("GET", url, params=querystring)

   
def main():
    PORT=3000
    server= HTTPServer(('',PORT),handler)
    print('%s'% PORT)
    server.serve_forever()

def response():
  url = "https://movie-database-alternative.p.rapidapi.com/"

  querystring = {"s":"Avengers Endgame","r":"json","page":"1"}

  headers = {
    "X-RapidAPI-Host": "movie-database-alternative.p.rapidapi.com",
    "X-RapidAPI-Key": "c796404f3dmsh382050b2263cf4cp19411djsn3deb0c68a138"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)

  print(response.text)
if __name__=='__main__':
  # main()
  response()
