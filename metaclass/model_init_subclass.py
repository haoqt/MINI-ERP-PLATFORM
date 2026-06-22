from miniorm.field import Field


class Model:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._fields = {k: v for k, v in vars(cls).items() if isinstance(v, Field)}


class Order(Model):
    name = Field(str)
    amount = Field(int)
    rate = Field(ftype=int, default=1)


if __name__ == '__main__':
    order = Order()
    print(f"order: {order}, _fields: {order._fields}")

# with __init_subclass_ version, the class structure is simple to read.
# when use it we can't change the type of namespace, but if we use metaclass, we can do this.
