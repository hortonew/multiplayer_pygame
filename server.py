import pygame
from pygame.locals import *
import socket
from classes import Character, Characters
import sys

class Server():
	def __init__(self):
		self.running = False
		self.clock = pygame.time.Clock()
		pygame.init()
		
		self.ip = self.ip = socket.gethostbyname(socket.gethostname())
		
		self.chs = Characters.Characters()
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_address = (self.ip, 1337)
		print >> sys.stderr, 'Starting server'
		self.sock.bind(server_address)
		self.sock.listen(1)
		
	def newCharacter(self, n, i):
		ch = Character.Character()
		ch.setName(n)
		ch.setIP(i)
		
		return ch
		
	def handleEvents(self):
		connection, client_address = self.sock.accept()
		try:
			print >>sys.stderr, 'connection from', client_address
		finally:
			connection.close()

	def start(self, fps=0):
		self.running = True
		self.fps = fps
		
		while self.running:
			self.handleEvents()
			
			self.clock.tick(self.fps)
			
fps = 30
s = Server()
s.start(fps)