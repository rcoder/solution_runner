def count(x):
	# returns a list from 1 to x
	nums = [i for i in range(1, x+1)]
	print(nums)
	return nums

class SquareInt():
	def __init__(num):
		self.int = num

	def square(self):
		return self.int * self.int
