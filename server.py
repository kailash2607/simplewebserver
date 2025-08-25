from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!doctype html>
<html>
<head>
<title> Table Name</title>
</head>
<body>
<table border="1" align = "center">
  <tr>
    <th>S.no</th>
    <th>Name of The Protocols</th>
    <th>Name of the Protocols</th>
  </tr>
  <tr>
    <td>1</td>
    <td>Application Layer/td>
    <td>Http,Ftp,DNS</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Transport Layer</td>
    <td>TCP/UDP</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Network Layer</td>
    <td>IPV4</td>
  </tr>
<tr>
    <td>4</td>
    <td>Link Layer</td>
    <td>Ethernet</td>
  </tr>
</table>
</body>
</html>'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()