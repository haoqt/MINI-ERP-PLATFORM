from functools import wraps


def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None

            for attempt in range(1, times + 1):
                try:
                    print(f"Attempt {attempt}")
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Failed: {e}")
                    last_exception = e

            raise last_exception

        return wrapper
    return decorator


counter = 0


@retry(times=3)
def unstable():
    global counter
    counter += 1
    if counter < 3:
        raise ValueError("Something wrong")
    return "Success!"


print(unstable())