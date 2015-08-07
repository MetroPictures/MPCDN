import logging, os, json

from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer

def cdn():
	logging.basicConfig(filename=os.path.join(os.getcwd(), "cdn.log.txt"), level=logging.INFO)

	with open(os.path.join(os.getcwd(), "config.json"), 'rb') as C:
		config = json.loads(C.read())

	authorizer = DummyAuthorizer()
	authorizer.add_anonymous(os.path.join(os.getcwd(), "metro_pictures"))

	handler = FTPHandler
	handler.authorizer = authorizer
	handler.banner = "DeepLab x Camille Henrot CDN"

	server = FTPServer((config['ip'], config['port']), handler)
	server.max_cons = 256
	server.max_cons_per_ip = 5

	server.serve_forever()

if __name__ == '__main__':
	cdn()
