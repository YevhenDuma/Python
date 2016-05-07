import daemon
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import urllib2
from BeautifulSoup import BeautifulSoup
import json
from collections import OrderedDict

url = "http://www.metacritic.com/game/playstation-3"
divName = 'product_basics stats'
addr="localhost"
port=8989

class RequestHandler(BaseHTTPRequestHandler):
    def _writeheaders(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_HEAD(self):
        self._writeheaders()

    def do_GET(self):
	global url
        global divName
        self._writeheaders()
        req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })

	if "/games/" in self.path:
            gameinfo = "Game not found"
            page = urllib2.urlopen(req).read()
            soup = BeautifulSoup(page)
            for game in soup.body.findAll('div', attrs={'class' : divName}):
                name = self.path.replace("/games/","")
                if urllib2.unquote(name)  == game.a.text:
                    gameinfo = json.dumps(({"title" : game.a.text, "score" : game.span.text}),indent=2)
            self.wfile.write("""<HTML><HEAD><TITLE>Simple page</TITLE></HEAD>
            <BODY>"""+ gameinfo + """</BODY></HTML>""")
        elif "/games" in self.path:
            result = []
            page = urllib2.urlopen(req).read()
            soup = BeautifulSoup(page)
            for game in soup.body.findAll('div', attrs={'class' : divName}):
                result.append({"title" : game.a.text})
            self.wfile.write("""<HTML><HEAD><TITLE>Simple page</TITLE></HEAD>
            <BODY>"""+ json.dumps(result, indent=2) + """</BODY></HTML>""")
        else:
            result = []
            page = urllib2.urlopen(req).read()
            soup = BeautifulSoup(page)
            for game in soup.body.findAll('div', attrs={'class' : divName}):
                result.append({"title" : game.a.text, "score" : game.span.text})
            self.wfile.write("""<HTML><HEAD><TITLE>Simple page</TITLE></HEAD>
            <BODY>"""+ json.dumps(result, indent=2)  + """</BODY></HTML>""")
serveraddr = (addr,port)
server = HTTPServer(serveraddr, RequestHandler)
daemon_context = daemon.DaemonContext()
daemon_context.files_preserve = [server.fileno()]

# Become a daemon process.
with daemon_context:
    server.serve_forever()
