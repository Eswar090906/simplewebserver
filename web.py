from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!doctype html>
<html>
<head>
<title> My Web Server</title>
</head>
<body>
<h1><center>Welcome</center></h1>

<table border="2" cellspacing="10" cellpadding="6">
<tr>
<th>Manufacturer</th><td>Lenovo</td>
</tr>
<tr>
<th>Edition</th><td>Windows 11</td>
</tr>
<tr>
<th>Processor</th><td>13th Gen Intel(R) Core(TM)</td>
</tr>
<tr>
<th>config</th><td>i5</td>
</tr>
<tr>
<th>RAM<th><td>16.0 GB</td>
</tr>
<tr>
<th>System Type</th><td>64-bit Operating System</td>
</tr>
<table>
</body>
</html>
'''

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