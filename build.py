from jinja2 import Template, Environment, FileSystemLoader
import shutil
import os.path
import SimpleHTTPServer
import SocketServer


loader = FileSystemLoader(['src/content', 'src/layout'])
env = Environment(loader=loader)

if os.path.isdir("build"):
    shutil.rmtree("build")
shutil.copytree("src/layout", "build")

for content_file in os.listdir("src/content"):
    template = env.get_template(content_file)
    with open("build/" + content_file, "w+") as destination_file:
        destination_file.write(template.render().encode('utf8'))

os.chdir("build")

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
