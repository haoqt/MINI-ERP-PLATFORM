from field import Field


class MetaModel(type):
    def __new__(cls, name, bases, namespace):
        # get fields name from namespace dict because field.name is not created at here, they're created after that.
        fields = {}
        for base in bases:  # gom field kế thừa trước
            fields.update(getattr(base, '_fields', {}))
        for k, v in namespace.items():  # chồng field khai báo mới
            if isinstance(v, Field):
                fields[k] = v
        namespace["_fields"] = fields
        return super().__new__(cls, name, bases, namespace)


class Model(metaclass=MetaModel):
    pass


class Order(Model):
    name = Field(str)
    amount = Field(int)
    rate = Field(ftype=int, default=1)


if __name__ == '__main__':
    order = Order()
    print(f"order: {order}, _fields: {order._fields}")
