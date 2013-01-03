class Characters():
	def __init__(self):
		self.character_list = []
		
	def addCharacter(self, c):
		self.character_list.append(c)
		
	def removeCharacter(self, c):
		self.character_list.remove(c)