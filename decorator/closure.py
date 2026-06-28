def make_counter():
    count = 0

    def increment():
        nonlocal count
        print(f"CALL COUNT: {count}")
        count += 1
        return count

    return increment


counter = make_counter()

counter()
counter()
print(counter.__closure__)
print(counter.__closure__[0].cell_contents)

funcs = [lambda: i for i in range(3)]

# funcs = []
# for i in range(3):
#     def f():
#         return i
#     funcs.append(f)

print([f() for f in funcs])

# at lambda, i is save at cell object, so when for to i == 2, cell content is 2 => functs is list of 2
# to fix this bugs, we need to update i value at each step
funcs = [lambda i=i: i for i in range(3)]
print([f() for f in funcs])
