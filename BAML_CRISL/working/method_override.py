from abc import ABCMeta

class Base(metaclass=ABCMeta):
    # simply allow additional args in base class
    def hello(self, name, *args, **kwargs):
        print("Hello", name)


class Derived(Base):
    # derived class also has unused optional args so people can
    # derive new class from this class as well while maintaining LSP
    def hello(self, name, age=None, *args, **kwargs):
        super(Derived, self).hello(name, *args, **kwargs)
        print('Your age is ', age)


b = Base()
d = Derived()

b.hello('Alice')  # works on base, without additional params
b.hello('Bob', age=24)  # works on base, with additional params
d.hello('Rick')  # works on derived, without additional params
d.hello('John', age=30)  # works on derived, with additional params
