"""
A class definition of the range-squared iterable.

In this module we break one of our naming conventions,
namely that class names should all start with capital
letters. That is because we want to compare them with
generators, which folowwing function naming conventions.

Note that we have 2 classes: an iterator class and an 
iterable class. Iterable classes work by returning a
new/fresh iterator each time on demand
"""

class range2iter(object):            # isse iterator bnana tha
    """Iterator class for squares of a range"""
    # Attribute _limit: end of range
    # Attribute _pos: current spot of iterator
      
    
    def getLimit(self):
        """
        The limit defining this range squares iterator.

        If the limit is n, this generator will iterate the
        numbers 0, 1, 4, ... (n-1)*(n-1)
        """
        return self._limit

    def __init__(self,n):
        """
        Initializes a squares iterator for the range 0 to n-1

#         Parameter n: The limiter for this iterator
#         Precondition: n is an int >= 0
#         """
        self._limit = n
        self._pos = 0

    def __next__(self):
        """
        Returns the next element in the iterable

        This method raises StopIteration when it reaches the
        end of the iteration. This will cause the for loop
        to stop.
        """
        if self._pos == self._limit:
            raise StopIteration()
        else:
            value = self._pos*self._pos
            self._pos += 1
            return value

def range2iter(n):
    """
    Generator that iterates the squares of numbers 0 to n-1

    Example: range2iter(5) iterates 0, 1, 4, 9, 16

    Parameter n: The limiter for this generator
    Precondition: n is an int >= 0
    """
    for x in range(n):
        yield x*x
        print(x)

class range2(object):   # iterator ka jada kaam hai
    """Iterable class for squares of a range
    """
    
    def __init__(self,n):
        """Initializes a squares iterable for the range 0 to n-1

        Parameter n: The limiter for this iterable
        Precondition: n is an int >= 0
        """
        self._limit = n
    
    def __iter__(self):
        """Returns a new iterator for this iterable"""
        return range2iter(self._limit)

