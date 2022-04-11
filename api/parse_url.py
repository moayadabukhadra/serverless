from http.server import BaseHTTPRequestHandler , HTTPServer
from urllib import parse






class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    path=self.path
    path_comp=parse.urlsplit(path)

    output=""
    output+="<html><body>"
    output+=f"""<h1>Serverless Functions</h1>
            <h2>Url parse </h2>
            <table style="border-color: black;">
                <tr>
                <th>
                    Task
                </th>
                
                <th>progress</th>
                
                </tr>
                <tr>
                <td>scheme</td>
                <td>{path_comp[0]}</td>
                </tr>
                 <tr>
                <td>netloc</td>
                <td>{path_comp[1]}</td>
                </tr>
                <tr>
                <td>path</td>
                <td>{path_comp[2]}</td>
                </tr>
            </table>  
            </body>
            </html>"""
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    self.wfile.write(output.encode())
  
    return
   
def main():
    PORT=3000
    server= HTTPServer(('',PORT),handler)
    print('%s'% PORT)
    server.serve_forever()

    


if __name__=='__main__':
  main()
