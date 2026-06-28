
def depends(*fields):
    def decorator(func):
        func._depends = fields
        return func
    return decorator


class Order:

    @depends('amount', 'rate')
    def _compute_total(self):
        return 0

    @depends('tax')
    def _compute_tax(self):
        return 0

    def normal_method(self):
        pass


def collect_depends(cls):
    result = {}
    # dir(cls) return the names of all attributes that the object has
    # callable(obj) Check if the object can be called using () .
    for name in dir(cls):
        obj = getattr(cls, name)
        if callable(obj) and hasattr(obj, '_depends'):
            result[name] = obj._depends

    return result


print(collect_depends(Order))


def collect_depends(cls):
    result = {}
    for klass in cls.__mro__:                 # đi từ con tới cha
        for name, obj in vars(klass).items(): # vars = __dict__, KHÔNG trigger descriptor
            if callable(obj) and hasattr(obj, '_depends') and name not in result:
                result[name] = obj._depends
    return result

