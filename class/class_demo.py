class Rail_Ticket(object):
	"""This class elaborates the ticketing for indian railway"""

	def __init__(self,nam,n,tn):
		self.name = nam
		self.ticket_number = n
		self.train_number = tn

	def ticket_pr(self):
		pass

	def station(self):
		pass

	def print_content(self):
		print(f"({self.name} {self.ticket_number} {self.train_number})")


if __name__ == '__main__':
	obj = Rail_Ticket("rashmi",1,5)
	print(obj)
	obj.print_content()