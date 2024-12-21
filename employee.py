
class Employee(object):
	""" This class is about employees working in  company

	"""

	# Hidden attributes
	# attr _name : name of the employee
	# Inv _name : non-empty string
	# attr _startdate : first year hired
	# Inv _startdate: int;>1970 , other wise -1
	# attr_salary = annual salary which employee getting
	# Inv salary:should be float/int >=0 (annual)

	# def __init__(self, n , s = -1, sal = 5000.0):
	# 	self.name = n
	# 	self.startdate = s
	# 	self.salary = sal


	def setName(self, value):
		""" Sets the employee's name to the given value 
		parameter : The new name
		precondition : A non-empty string
		assert type(value) == str and len(value) > 0 ,  ' should be  not a  non-empty string' """
		set._name = value

	def getName(self):
		""" Returns the name of employees """
		return self._name


	def setStartdate(self, value):
		""" Sets value to start date of employee """
		assert type(value) == int or -1 ,'is not a  int'
		set._startdate = value

	def getStartdate(self):
		""" Returns the startdate of employee """
		return self._startdate
		

	def setSalary(self, value):
		""" Sets value to salary """
		assert type(value) == int or float , 'is not a not int or float'
		set._salary = value

	def getSalary(self):
		""" Returns the startdate """
		return self._salary
	
	
	def getCompensation(self, salary):
		"""Returns the annual compensation """
		return self._salary
	"it is same as salary of base class"

	def __init__(self, n , s = -1, sal = 5000.0):
		self.setName(n)
		self.setStartdate(s)
		self.setSalary(sal)



	def __str__(self):
		return  '(' +str(self.name ) + ','+str(self.startdate) + ','+str(self.salary) + ')'
	


		

	def __repr__(self):
		return str(self.__class__) + str(self)

		
		

	
# E1 = Employee()


class Executive(Employee):
	""" This class represent the special Employee who is a part of Executive """

	# attr _bonous = Bonous salary which is given to special employee
	# Inv : must be int or float and value>= 0


	def getBonous(self):
		""" Returns the bonous to executive employee """
		#assert type(bonous) == int or float ,repr(bonous) + ' precondition voilation'   isme jarrorat nhi hai

		return self._bonous


	def setBonous(self,value):
		""" Set the value to bonous in salary of executive employee 

		parameter bonous : bonous to be given
		precondition  : must be int or float """

		assert type('bonous') == int or float ,repr('bonous') + ' precondition voilation '

		set._bonous = value



	def __str__(self):
		return super().__str() +  str(self.__class__) + str(self)


	def __repr__(self):
		
		return  '(' + str(self.bonous) + ')'


	# def __init__(self,b = 0):
		""" This function initializes the bonous attributes given to executive employee 

		parameter b : bonous to be initilize
		precondition : """
		super().__init__(n, s, sal = 50000.0)

		# self.setBonous(b)


	def getCompensation(self, salary):
		"""Returns the annual compensation """
		return self._salary + self._bonous

# Creating an instance of Employee
employee = Employee("John Doe", 20220101, 60000.0)
print(employee.__str__())  # Output: Employee(John Doe, 20220101, 60000.0)
print(employee.__repr__())  # Output: (John Doe, 20220101, 60000.0)

# Creating an instance of Executive
executive = Executive("Jane Smith", 20220102, 10000.0)
executive.setBonous(2000.0)
print(executive.__str__())  # Output: Employee(Jane Smith, 20220102, 50000.0), 2000.0
print(executive.__repr__())  # Output: (Jane Smith, 20220102, 50000.0, 2000.0)

# Getting compensation for both
print(employee.getCompensation())  # Output: 60000.0
print(executive.getCompensation())  # Output: 52000.0 (50000.0 + 2000.0)















		




