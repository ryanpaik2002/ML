import time

def time_deco(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper


# sample call
# @time_deco
# def some_func():
#     time.sleep(3)

# some_func()


