from http.server import BaseHTTPRequestHandler , HTTPServer

import calendar
from datetime import datetime










class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    path=self.path
    cal=calendar.HTMLCalendar(firstweekday = 0)
    
    current_date = datetime.now()
    current_date.strftime('%A')
    output=""
    output+=""
    output+=f"<h2>Today is {current_date.strftime('%A')}</h2>"
    output+=f"""
    <h2>Todays time: {datetime.time(datetime.today())}</h2>
    
    <h2>Todays Date: {datetime.date(datetime.today())}</h2>
    """
    output+=f"""{cal.formatyear(2022)}"""
    
    
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
