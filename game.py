import cmd

class Game(cmd.Cmd):
	def __init__(self):
		cmd.Cmd.__init__(self)
		
	def do_n(self, args):
		"""Go north"""
		
	def do_s(self, args):
		"""Go south"""
		
	def do_e(self, args):
		"""Go east"""

	def do_w(self, args):
		"""Go west"""
		
	def do_quit(self, args):
		print("End of game")
		return True
		
if __name__ == "__main__":
	g = Game()
	g.cmdloop()