from classes import Character, Characters
from gevent import socket
from gevent.server import StreamServer

class Server():
	def __init__(self):
		
		#get server ip (current machine)
		self.ip = self.ip = socket.gethostbyname(socket.gethostname())
		print "Starting server: %s:1337" % self.ip
		
		self.chs = Characters.Characters()
		
	#take data from client and return new positions
	def update():
		pass
	
	def clientConnect(self, sock, address):
		l = len(self.chs.character_list)
		newch = self.newCharacter(l+1, address[0])
		self.chs.addCharacter(newch)

		#create file object to talk to socket
		fp = sock.makefile()
		while True:
			line = fp.read(1)
			if line:
				print l, " - IP: ", address[0], ". Port: ", address[1], ". ", line
			else:
				break
		#close connection and remove character from character list
		sock.shutdown(socket.SHUT_WR)
		sock.close()
		self.chs.removeCharacter(newch)
		print "Closing connection to: ", address[0]
		
	#return character object
	def newCharacter(self, id, ip):
		ch = Character.Character(id, ip)
		return ch

	#start server
	def start(self):
		server = StreamServer( ('', 1337), self.clientConnect)
		server.serve_forever()
			
s = Server()
s.start()