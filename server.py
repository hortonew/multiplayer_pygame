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
		
	def echo(self, sock, address):
		fp = sock.makefile()
		while True:
			line = fp.readline()
			if line:
				print address
				print line
				fp.write(line)
				fp.flush()
			else:
				break
		sock.shutdown(socket.SHUT_WR)
		sock.close()
		
	def newCharacter(self, n, i):
		ch = Character.Character()
		ch.setName(n)
		ch.setIP(i)
		
		return ch
		
	def handleEvents(self):
		pass

	def start(self, fps=0):
		self.running = True
		self.fps = fps
		server = StreamServer( ('', 1337), self.echo)
		server.serve_forever()
		
		while self.running:
			self.handleEvents()
			self.clock.tick(self.fps)
			
fps = 30
s = Server()
s.start(fps)