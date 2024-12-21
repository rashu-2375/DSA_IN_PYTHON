
# class Instructor:
# 	def __init__(self,name):
# 		self.name = name

# 		print("creating a new object")
    
# instructor_1 =Instructor("Rashmi")
# print(instructor_1.name)


# instructor_2 =Instructor("Rashu")
# # instructor_2.name = "rashu"
# print(instructor_2.name)

class Dog(object):
	def __init__(self, name, breed, age, color):
		self.name = name
		self.breed = breed
		self.age = age
		self.color = color

	def __str__(self):
		return '(' + str(self.name) + ',' + str(self.breed) + ',' + str(self.age) +',' + str(self.color) + ')'
	def _repr__(self):
		return str(self.__class__) + str(self)
	
D1 = Dog("Tommy",'German sheferd', 4, 'brown')
print(str(D1))
print(D1.__str__())
print(repr(D1))
print(D1.__repr__())

class Vehicle(object):
	def __init__(self, brand, model, type):
		self.brand = brand
		self.model = model
		self.type = type

	def __str__(self):
		return '(' + str(self.brand) + ',' + str(self.model) + ',' + str(self.type) + ')'
	def __repr__(self):
		return str(self.__class__) + str(self)
v1 = Vehicle("bmw",2024, 'four wheeler')
print(str(v1))
print(repr(v1))
		