from typing import Any
# Built-in Classes

# Creating instances from bultins

int('1')  # Creates 1
str(1)  # Creates '1'

dict([[1, 2], [3, 4]])  # creates {1: 2, 3: 4}
dict(first='a', last='b')  # Creates {'first': 'a', 'last': 'b'}
tuple('example')  # creates ('e', 'x', 'a', 'm', 'p', 'l', 'e')
list('example')  # creates ['e', 'x', 'a', 'm', 'p', 'l', 'e']
set([1, 2, 3, 2, 1])  # creates {1,2,3}


# Custom class


class A:
    def __init__(self) -> None:
        # The first argument of all instance methods refers
        # to the instance itself.
        # by convention it is named `self`,
        # but it could be named anything
        pass

    def pica(this):
        print('pica', end='')
        # for the Java fans! But seriously, do not do this :P
        return this

    def boo(self):
        # Even if not used, the instance method signature is still required
        # to take the instance has its first argument.
        print('boo!')


print(A().pica().boo())  # prints picaboo!

# All classes inherits from `object`
print(isinstance(A(), object))  # Prints True


class Being():
    # class variable
    count = 0
    health = 50

    def __init__(self, health=100):

        # If the same attibute name is defined in both
        # instance and class, the lookup prioritizes
        # the instance.        self.health = health  # instance variable
        Being.count += 1

    # def __new__(cls, *args, **kwds) -> Any:
    #     """Acts as middleware for instance initialization"""
    #     print('new', cls, args, kwds)
    #     cls.__init__(cls, *args, **kwds)
    #     Being.count += 1
    #     print('Population increased:', Being.count)
    #     return cls

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """Make the class instance callable"""
        print('Thanks, __call__!')
        print('Says:', args, kwds)

    def __del__(self):
        Being.count -= 1


print(Being.count)  # prints 0


def world():
    x = Being(1)
    x()
    print('Health of x', x.health)
    print('Being count:', Being.count)  # prints 1
    y = Being(2)
    # prints 2


world()
print('Being count:', Being.count)
