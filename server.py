import pygame
from pygame.locals import *
from classes import Character, Characters
from gevent import socket
from gevent.server import StreamServer

class Server():
	def __init__(self):
		self.running = False
		self.clock = pygame.time.Clock()
		pygame.init()
		
		self.ip = self.ip = socket.gethostbyname(socket.gethostname())
		print "Starting server: %s:1337" % self.ip
		
		self.chs = Characters.Characters()
		
	def update():
		pass
	
	def clientConnect(self, sock, address):
		l = len(self.chs.character_list)
		newch = self.newCharacter(l+1, address[0])
		self.chs.addCharacter(newch)

		fp = sock.makefile()
		while True:
			line = fp.read(1)
			if line:
				print l, " - IP: ", address[0], ". Port: ", address[1], ". ", line
			else:
				break
		sock.shutdown(socket.SHUT_WR)
		sock.close()
		self.chs.removeCharacter(newch)
		print "Closing...", address[0]
		
	def newCharacter(self, id, ip):
		ch = Character.Character(id, ip)
		return ch
		
	def handleEvents(self):
		pass

	def start(self, fps=0):
		self.running = True
		self.fps = fps
		server = StreamServer( ('', 1337), self.clientConnect)
		server.serve_forever()
		
		while self.running:
			self.handleEvents()
			self.clock.tick(self.fps)
			
fps = 30
s = Server()
s.start(fps)