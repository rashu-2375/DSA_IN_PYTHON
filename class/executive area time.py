class Time(object):
    """Class to reprsent times of a day.

    Inv : hour is an int in 0..23
    Inv:  min is an int in 0..59"""
 
    def __init__(self, hour, min):
        """the time  hour: min.
        Pre : hour in 0..23 ; min in 0..59"""
        # self.hour = hour
        # self.min = min
        self.setHour(hour)
        self.setMin(min)
        self.__sec = 60


        
    def increment(self, hours, mins):
        """Move time hours and min into  future
        Pre: hours int >= 0; mins in 0..59"""
        self.hour += hours + self.min // 60
        self.mins += mins % 60
    
    def setHour(self, value):
        """sets hour to value"""
        self._hour = value
        
    def getHour(self):
        return self._hour
    
    def setMin(self, value):
        """sets hour to value"""
        self._min = value

    def getMin(self):
        return self._min

    def setSec(self, value):
        self._sec = value

    def getSec(self):
        return self.__sec
    
# t = Time(2,30)
# t.hour = 4
# t.setHour(5)
# print(t._hour)
# print(t.getMin())
# t.setMin(70)
# print(t._min)
# # print(t.__sec)
# print(t.getSec())

class Employee(object):
    # INSTANCE ATTRIBUTES:
    # _name: full name, a non-empty string
    # _start: year of hiring, an int ≥ 1965, -1 if unknown
    # _salary: yearly wage, a float, -1 if unknown
    
    def getName(self):
        """returns the employee name"""
        return self._name

    def setName(self, value):
        """sets the name of employee to this value
        it is a non-empty string"""
        assert value is None or type(value) == str
        self._name = value

    def getStart(self):
        """returns the employee hiring year"""
        return self._start

    def setStart(self, value):
        """sets the start year of employee to this value
        it is a non-empty integer value"""
        assert value is None or (type(value) == int and value >= 1965)
        self._start = value

    def getSalary(self):
        """returns the employee Salary"""
        return self._salary

    def setSalary(self, value):
        """sets the salary of employee to this value
        it is a non-negative float value"""
        assert value is None or (type(value) == float and value >= 0)
        self._salary = value

    def getCompensation(self):
        """returns the annual compensation 
        it is same as the salary for the base employee"""
        return self._salary

    def setCompensation(self, value):
        """sets the compensation to this value"""
        assert value is None or (type(value) == float and value >= 0)
        self._salary = value

    def _init_(self, name, start, salary):
        """here initializing the name, salary, start year"""
        self.setName(name)
        self.setStart(start)
        self.setSalary(salary)

    def _str_(self):
        return '(' + str(self._name) + ',' + str(self._start) + ',' + str(self._salary) + ')'

    def _repr_(self):
        return str(self._class_) + str(self)


class Executive(Employee):
    # INSTANCE ATTRIBUTES:
    # _bonus: yearly bonus, a float, -1 if unknown
    # _salary: yearly wage, a float, -1 if unknown

    def getBonus(self):
        """returns bonus for executive"""
        return self._bonus

    def setBonus(self, value):
        """sets the bonus of executive to this value
        it is a non-negative float value"""
        assert value is None or (type(value) == float and value >= 0)
        self._bonus = value

    def getCompensation(self):
        """returns the annual compensation for executive 
        it is the sum of salary and bonus"""
        return self._salary + self._bonus

    def setCompensation(self, value):
        """sets the compensation to this value"""
        assert value is None or (type(value) == float and value >= 0)
        self._salary = value

    def _init_(self, name, start, salary, bonus):
        """initializing the name, salary, start year, and bonus for executive"""
        super()._init_(name, start, salary)
        self.setBonus(bonus)

    def _str_(self):
        return super().__str__() + ',' + str(self._bonus)

    def _repr_(self):
        return str(self.__class__) + str(self) 
    
# Create an Employee object
employee = Employee("John Doe", 1980, 50000.0)

# Accessing and printing employee details
print("Employee details:", employee)
print("Compensation:", employee.getCompensation())
print("Name:", employee.getName())
print("Joining Year:", employee.getStart())
print(str(employee))
print(repr(employee))



# Create an Executive object
executive = Executive("Jane Smith", 1990, 80000.0, 10000.0)
# Accessing and printing executive details
print("Executive details:", executive)
print("Compensation:", executive.getCompensation())
print("Salary:", executive.getSalary())
print(str(executive))
print(repr(executive))

