# class MyClass:
#     def __init__(self, value):
#         assert value >= 0, "Value must be non-negative"
#         self.value = value

#     def perform_action(self):
#         assert self.value >= 10, "Value must be at least 10 to perform this action"
#         # rest of the method logic
# obj = MyClass(-5)
# obj.perform_action()


class Example:
    a = 29  # Class attribute

# Creating an instance of the Example class
e = Example()

# Adding object attribute
e.b = 42

# Accessing class attribute from object
print(e.a)  # Output: 29

# Modifying class attribute from object (creates object attribute)
e.a = 10

# Accessing object attribute (overrides class attribute)
print(e.a)  # Output: 10


# import math
# class Point3(object):
#     """Class for points in 3D space.
    
#     Invariants:
#     - x is a float
#     - y is a float
#     - z is a float
#     """

#     def distance(self, q):
#         """Returns distance from self to q.

#         Precondition: q is a Point3.
#         """
#         assert type(q) == Point3
#         sqrdst = ((self.x - q.x) ** 2 + (self.y - q.y) ** 2 + (self.z - q.z) ** 2)
#         return math.sqrt(sqrdst)

# class computer:
#     pass
# c1 = computer()
# c2 = computer()

# print(id(c1))  # get address of the memory
# print(id(c2)) 

class computer:
    n = "Navin"
    a = '28'
    def _init__(self,n,a):
        self.name = n
        self.age = a
c1 = computer()
c2 = computer()


print(c1.n)
print(c2.a)
        



        

