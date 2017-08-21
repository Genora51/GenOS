from http.server import SimpleHTTPRequestHandler,HTTPServer
import re
from os.path import join
from jinja2 import Environment, FileSystemLoader, select_autoescape, TemplateNotFound

appreg = re.compile(r'^((/apps/[\w]+\.gex/?)|(/(index\.html)?))$')

port = 8000
env = Environment(
    loader=FileSystemLoader(['./apps', './']),
    autoescape=select_autoescape(['html', 'xml'])
)

class myHandler(SimpleHTTPRequestHandler):

    #Handler for the GET requests
    def do_GET(self):
        if appreg.match(self.path):
            self.do_app()
        else:
            super(myHandler, self).do_GET()

    def do_app(self):
        pth = self.path.strip('/')
        try:
            with open((pth + '/options.txt').strip('/')) as f:
                options = dict(
                    tuple(l.strip('\n').split(' : ')) for l in f
                )
        except (FileNotFoundError, TemplateNotFound):
            options = {}
        template = env.get_template((pth.strip('/apps') + '/index.html').strip('/'))
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(template.render(options=options).encode('UTF-8'))


server = HTTPServer(('', port), myHandler)
print('Started httpserver on port ', port)

#Wait forever for incoming http requests
server.serve_forever()