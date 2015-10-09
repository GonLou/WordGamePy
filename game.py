import cmd
import textwrap
import room
from openpyxl import load_workbook

#https://docs.google.com/spreadsheets/d/1Z24N7mSTCwnemRWJzFwy86Fepv6Nw0xrH5ky4x0bY04/edit?usp=sharing
#name	description	Nvalue	Svalue	Evalue	Wvalue

#https://docs.google.com/spreadsheets/d/1oLr3DZA4KWR8YrN73oH6NXhjB97LGkdMiy_m7TG42pI/edit?usp=sharing

class Game(cmd.Cmd):
	def __init__(self):
		cmd.Cmd.__init__(self)
		
		#doc = gc.open_by_url('https://docs.google.com/spreadsheets/d/1Z24N7mSTCwnemRWJzFwy86Fepv6Nw0xrH5ky4x0bY04/edit?usp=sharing')
		
		wb2 = load_workbook('WordGamePyData.xlsx')
		print wb2.get_sheet_names()
		#['Sheet2', 'New Title', 'Sheet1']
		
		self.loc = room.Room(id=1, name="Hall", description="asasdad", neighbours={'w':2})
		self.look()
		
	def move(self, dir):
		newroom = self.loc._neighbour(dir)
		if newroom is None:
			print("Hummm that is not the way!")
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