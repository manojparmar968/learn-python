def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('hello world')
        res = func(*args, **kwargs)
        if res is not None:
            print(res)
        print('bye bye')
    return wrapper

@my_decorator
def my_function():
    print('we are running ...')

@my_decorator
def calculate(x, y):
    return x + y

my_function()
calculate(2, 3)


# authenticated = False
# numbers = [x for x in range(101)]

# def is_auth(func):
#     def wrapper(num_list):
#         if not authenticated:
#             print("access denied")
#         else:
#             print('works')
#             res = func(num_list)
#             print('result', res)
#             print('done')
#     return wrapper

# @is_auth
# def calculate_sum(num_list):
#     sum = 0
#     for num in num_list:
#         sum += num
#     return sum

# calculate_sum(numbers)

# import time

# def timer(func):
#     def wrapper(p_time):
#         start = time.time()
#         print('starting...')
#         func(p_time)
#         total = time.time() - start
#         print('done', total)
#     return wrapper

# @timer
# def do_something(pause):
#     time.sleep(pause)
#     print('hello world')

# do_something(1)
# do_something(5)
# do_something(3)