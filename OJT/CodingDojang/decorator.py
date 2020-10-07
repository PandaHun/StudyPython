from functools import wraps

def my_decorator(func):
    print('my_decorator exec')
    @wraps(func)
    def runs_func():
        print('runs_funs_exec')
        print("This is ")
        func()
        print("blog")
    return runs_func


@my_decorator
def my_func():
    print('my_func exec')
    print("yaboong's ")

print('call my_func')
my_func()