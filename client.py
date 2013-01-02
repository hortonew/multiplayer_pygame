import pygame
from pygame.locals import *
import socket
import sys

WINDOW_SIZE = (800, 600)

class Client():
	def __init__(self):
		self.running = False
		self.clock = pygame.time.Clock()
		pygame.init()
		
		self.screen = pygame.display.set_mode(WINDOW_SIZE)
		self.w, self.h = WINDOW_SIZE[0], WINDOW_SIZE[1]
		self.screen.fill((255,255,255))
		pygame.display.flip()
		
		
		self.ip = socket.gethostbyname(socket.gethostname())
		print "Client IP: %s" % self.ip
		#self.serverip = raw_input("What is the server IP address?\n\n")
		self.serverip = '192.168.1.100'
		print "\n-----------------------\n\n"
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_address = (self.serverip, 1337)
		print >>sys.stderr, 'connecting to server'
		self.sock.connect(server_address)
		self.name = raw_input("What is your username?\n\n")
		print "\n-----------------------\n\n"
	
	def keyDown(self, key):
		if key == K_w:
			print 'w'
		if key == K_a:
			print 'a'
		if key == K_s:
			print 's'
		if key == K_d:
			print 'd'
	
	def handleEvents(self):
		keys = pygame.key.get_pressed()
		if keys[K_w]:
			self.keyDown(K_w)
		elif keys[K_s]:
			self.keyDown(K_s)
		elif keys[K_a]:
			self.keyDown(K_a)
		elif keys[K_d]:
			self.keyDown(K_d)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.running = False
			
	def start(self, fps=0):
		self.running = True
		self.fps = fps
		
		while self.running:
			self.handleEvents()
			pygame.display.flip()
			self.clock.tick(self.fps)
		self.sock.close()
		pygame.quit()
		sys.exit()
			
fps = 30
c = Client()
c.start(fps)