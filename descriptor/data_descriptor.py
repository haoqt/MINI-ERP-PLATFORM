class Typed:
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        print(f"CALL SET NAME: owner: {owner}, name: {name}")
        self.private = f"_{name}"

    def __get__(self, instance, owner):
        print("CALL GETTER")
        if self.private in instance.__dict__:
            return instance.__dict__[self.private]
        return "Not found"

    def __set__(self, instance, value):
        print("CALL SETTER")
        if not isinstance(value, self.expected_type):
            raise TypeError(f"{self.private} expects {self.expected_type.__name__}, got {type(value).__name__}")
        instance.__dict__[self.private] = value

    def __delete__(self, instance):
        print("CALL DELETER")
        del instance.__dict__[self.private]


class Order:
    field_A = Typed(str)
    field_B = Typed(int)


if __name__ == '__main__':
    order = Order()
    order.field_A = "this is char"
    print(f"order.__dict__: {order.__dict__}")
    order.field_B = "10"
    print(f"order.__dict__: {order.__dict__}")
    del order.field_A
    del order.field_B
