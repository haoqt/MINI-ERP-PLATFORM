class Field:
    def __init__(self, ftype=None, default=None, required: bool = False):
        self._ftype = ftype
        self._default = default
        self._required = required

    def __set_name__(self, owner, name):
        self.name = name
        self.attname = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self

        if self.attname not in instance.__dict__:
            return self._default

        return instance.__dict__[self.attname]

    def __set__(self, instance, value):
        if value is not None and not isinstance(value, self._ftype):
            raise TypeError("Field must be of type %s" % self._ftype)
        instance.__dict__[self.attname] = value

    # TODO: process for required


def get_amount(self):
    return 50


Order = type('Order', (), {'name': Field(str), 'get_amount': get_amount})


if __name__ == '__main__':
    order = Order()
    print(f"order: {order}, name: {order.name}, get_amount: {order.get_amount()}")
