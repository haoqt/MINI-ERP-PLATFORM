# Method Resolution Order ( Class.__mro__ )
# 1. Data Descriptor
# 2. instance.__dict__
# 3. Non-data descriptor
# 4. Class.__dict__
# 5. Parent Classes theo __mro__
# 6. __getattr__()

class A:
    name = "A"


class B(A):
    pass


class C(B):
    pass


class A1:
    name = "A"


class B1:
    name = "B"


class C1(A1, B1):
    pass


class ClassX:
    x = 10


if __name__ == '__main__':
    print(f"C.__mro__: {C.__mro__}")
    c = C()
    # c.__dict__ -> C -> B -> A -> object
    print(f"c.name: {c.name}")

    print(f"C1.__mro__: {C1.__mro__}")
    c1 = C1()
    # c1.__dict__ -> C1 -> A1 -> object
    print(f"c1.name: {c1.name}")

    # instance.__dict__
    print(f"ClassX.__mro__: {ClassX.__mro__}")
    x = ClassX()
    print(f"x.__dict__: {x.__dict__}")
    print(f"ClassX.__dict__: {ClassX.__dict__}")
    print(f"x.x: {x.x}")
    x.x = 20
    print(f"x.__dict__: {x.__dict__}")
    print(f"ClassX.__dict__: {ClassX.__dict__}")
    print(x.x)


# class SaleOrder(models.Model):
#     _inherit = "sale.order"
#     def action_confirm(self):
#         ...
#         print(type(self).__mro__) => in toàn bộ chuỗi class mà Python duyệt khi tìm
