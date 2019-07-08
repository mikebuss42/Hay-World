import random


class HayWorld(object):
	def __init__(self, size):
		self.size = size
		self.state_space = [["" for i in range(0, size)] for j in range(0, size)]
		print("Generated state space with {} cols and {} rows".format(len(self.state_space), len(self.state_space[0])))
		self.generate_needle()

	def state(self, row, col):
		return self.state_space[row][col] == "x" # x will represent the needle in the haystack
	
	def generate_needle(self):
		r = random.randint(0, self.size -1) 
		c = random.randint(0, self.size -1)
		self.state_space[r][c] = "x"
		print("Generated a needle at pos {}, {}".format(r, c))

	def find_path(self):
		open_states = [(0, 0)]
		closed_states = []
		while len(open_states) != 0:
			print("Open: {:<75}; Closed: {}".format(str(open_states), str(closed_states)))
			x = open_states.pop(0)
			closed_states.append(x)
			r = x[0]
			c = x[1]
			if self.state(r, c):
				return x
			else:
				children_grids = []
				for cords in [(r+1, c), (r+1, c+1), (r, c+1)]:
					if cords[0] < self.size and cords[1] < self.size:
						children_grids.append(cords)
				for c in children_grids:
					if c not in open_states and c not in closed_states:
						open_states.append(c)

	@classmethod
	def main(cls):
		h = HayWorld(4)
		h.find_path()


if __name__ == "__main__":
	HayWorld.main()

