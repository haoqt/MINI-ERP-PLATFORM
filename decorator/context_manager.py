class Transaction:
    def __enter__(self):
        print("BEGIN")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("COMMIT")
        else:
            print("ROLLBACK")
        # Khong nuot exception
        return False


with Transaction():
    print("INSERT")
    print("UPDATE")

print('--------------------')
try:
    with Transaction():
        print("INSERT")
        raise ValueError("Something wrong")
except Exception as e:
    print(f"Catch outside: {e}")

print('--------------------')


from contextlib import contextmanager


@contextmanager
def transaction():
    print("BEGIN")
    try:
        yield
        print("COMMIT")
    except Exception:
        print("ROLLBACK")
        raise


with transaction():
    print("INSERT")

print('--------------------')
try:
    with transaction():
        print("INSERT")
        raise ValueError("Oops")
except Exception:
    print("Catch outside")
