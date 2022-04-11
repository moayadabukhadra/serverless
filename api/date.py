from http.server import BaseHTTPRequestHandler , HTTPServer


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    #  request is successful and you will get your response
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    output=''
    output+="""<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>"""
    output+="""<h1>Serverless Functions</h1>
            <h2>Tasks</h2>
            <table style="border-color: black;">
                <tr>
                <th>
                    Task
                </th>
                
                <th>progress</th>
                
                </tr>
                <tr>
                <td>Sign up with Vercel</td>
                <td>Done</td>
                </tr>
                 <tr>
                <td>Create a repository on Github and link it to Vercel account</td>
                <td>Done</td>
                </tr>
                <tr>
                <td>Create a simple html front end to interact with serverless function</td>
                <td>Done</td>
                </tr>
            </table>  
            </body>
            </html>"""

    self.wfile.write(output.encode())
    return

# def main():
#     PORT=3000
#     server= HTTPServer(('',PORT),handler)
#     print('%s'% PORT)
#     server.serve_forever()

# if __name__=='__main__':
#     main()
