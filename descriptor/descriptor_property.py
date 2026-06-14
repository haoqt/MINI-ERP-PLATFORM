class my_property:

    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        print("CALL __get__")
        if instance is None:
            return self

        if self.fget is None:
            raise AttributeError("unreadable attribute")

        return self.fget(instance)

    def __set__(self, instance, value):
        print("CALL __set__")
        if self.fset is None:
            raise AttributeError("can't set attribute")

        self.fset(instance, value)

    def __delete__(self, instance):
        print("CALL __delete__")
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel)

class Person:

    def __init__(self, name=None):
        self._name = name

    @my_property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


if __name__ == '__main__':
    person = Person()
    print(person.name)
    person.name = "Visnu"
    print(person.name)

