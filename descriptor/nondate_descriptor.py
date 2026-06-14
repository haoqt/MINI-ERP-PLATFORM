class LazyProperty:
    def __init__(self, func=None):
        self.func = func

    def __set_name__(self, owner, name):
        self.__name__ = name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        if self.__name__ not in instance.__dict__:
            instance.__dict__[self.__name__] = self.func(instance)
            return instance.__dict__[self.__name__]
        return instance.__dict__[self.__name__]


class Field:
    @LazyProperty
    def value(self):
        print("CALL COMPUTE VALUE")
        return 10 * 5


if __name__ == '__main__':
    field = Field()
    print(f"FiRST CALL")
    print(f"field.value: {field.value}")
    print(f"SECOND CALL")
    print(f"field.value: {field.value}")

