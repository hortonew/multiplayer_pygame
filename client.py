import pygame
from pygame.locals import *
from gevent import socket
import sys
from twisted.internet import reactor, protocol
from twisted.internet.task import LoopingCall

DESIRED_FPS = 30.0
WINDOW_SIZE = (800, 600)

class EchoClient(protocol.Protocol):
	def __init__(self, d):
		print 'client says %s' % d

	def connectionMade(self):
		print "connected"
		self.transport.write("hello, world!")
		self.transport.loseConnection()	

	def dataReceived(self, data):
		#As soon as any data is received, write it back.
		print "Server said:", data

	def connectionLost(self, reason):
		print "connection lost"
		

class EchoFactory(protocol.ClientFactory):

	def __init__(self, d):
		self.data = d
	
	#uses EchoClient as the protocol, allowing the passing of parameters 
	#could have just done protocol=EchoClient
	def buildProtocol(self, addr):
		return EchoClient(self.data)

	def clientConnectionFailed(self, connector, reason):
		print "Connection failed - shutting down!"
		reactor.stop()

	def clientConnectionLost(self, connector, reason):
		print "Connection lost - disconnecting!"
		#reactor.stop()

class Client():
	def __init__(self):
		pygame.init()
		
		self.screen = pygame.display.set_mode(WINDOW_SIZE)
		self.w, self.h = WINDOW_SIZE[0], WINDOW_SIZE[1]
		self.screen.fill((255,255,255))
		pygame.display.flip()
		
		
		self.ip = socket.gethostbyname(socket.gethostname())
		print "Client IP: %s" % self.ip
		#self.serverip = raw_input("What is the server IP address?\n\n")
		self.serverip = '192.168.1.100'
		self.serverport = '1337'
		print "\n-----------------------\n\n"
		
	
	def keyDown(self, key):
		if key == K_w:
			print 'w'
			command = 'w'
		if key == K_a:
			print 'a'
			command = 'a'
		if key == K_s:
			print 's'
			command = 's'
		if key == K_d:
			print 'd'
			command = 'd'
			
		f = EchoFactory(command)
		reactor.connectTCP("192.168.1.100", 1337, f)
	
	def handleEvents(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w:
					self.keyDown(K_w)
				elif event.key == pygame.K_s:
					self.keyDown(K_s)
				elif event.key == pygame.K_a:
					self.keyDown(K_a)
				elif event.key == pygame.K_d:
					self.keyDown(K_d)
				elif event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
					
	def game_tick(self):
		#print 'tick'
		self.handleEvents()
		self.draw()
		
	def draw(self):
		pygame.display.flip()
			
	def start(self):

		#twisted clock
		tick = LoopingCall(self.game_tick)
		tick.start(1.0 / DESIRED_FPS)

		reactor.run()

c = Client()
c.start()