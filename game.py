import cmd
import textwrap
import room

class Game(cmd.Cmd):
	def __init__(self):
		cmd.Cmd.__init__(self)
		
		self.loc = room.Room(id=1, name="Hall", description="asasdad", neighbours={'w':2})
		self.look()
		
	def move(self, dir):
		newroom = self.loc._neighbour(dir)
		if newroom is None:
			print("You are forbidden to go that way!")
		else:
			""""self.loc = get_room(newroom)"""
			self.look()
	
	def look(self):
		print(self.loc.name)
		print("")
		for line in textwrap.wrap(self.loc.description, 70):
			print(line)
		
	def do_n(self, args):
		"""Go north"""
		self.move('n')
		
	def do_s(self, args):
		"""Go south"""
		self.move('s')
		
	def do_e(self, args):
		"""Go east"""
		self.move('e')

	def do_w(self, args):
		"""Go west"""
		self.move('w')
		
	def do_quit(self, args):
		print("End of game")
		return True
		
if __name__ == "__main__":
	Game().cmdloop()