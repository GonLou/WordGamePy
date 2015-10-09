class Room():
	def __init__(self, id=0, name="A chamber", description="An empty chamber", neighbours={}):
		self.id = id
		self.name = name
		self.description = description
		self.neighbours = neighbours
		
	def _neighbour(self, direction):
		if direction in self.neighbours:
			return self.neighbours[direction]
		else:
			return None
	
	def north(self):
		return self._neighbour("n")

	def south(self):
		return self._neighbour("s")

	def east(self):
		return self._neighbour("e")

	def west(self):
		return self._neighbour("w")		