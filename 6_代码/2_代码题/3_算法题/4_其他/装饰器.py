
# https://blog.csdn.net/beichanbb/article/details/125707327

# 没有参数的，简单的
def debug(func):
    def wrapper():
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func()
    return wrapper

@debug
def hello():
    print ("hello!")

# 不带参数
import time
def decorator(func):
    """实现一个普通装饰器，打印每次函数开始执行的时间"""
    def wrapper(*args, **kwargs):
        excu_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        print(f"当前函数 {func.__name__} 的执行时间是:{excu_time}")
        print(*args)
        return func(*args, **kwargs)
    return wrapper

@decorator  # 等价于 func2 = decorator(func2)
def func2(r):
    print("python 函数装饰器")

func2("t")


# 带参数简单
def wrapper(i):
    def log(func):
        def inner():
            print(i)
            print("func log")
            return func()
        return inner
    return log

@wrapper(i=1)
def hello():
    print("hello")

hello()


# 如果装饰器函数本身带参数，那么我们需要在原装饰器之上再定义一层，用来接收装饰器本身的参数
# def decorator(para):
#     """ 实现一个带参数的装饰器，在函数每次执行之前打印一句话 """
#     print(f'hello {para}')
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             return func(*args, **kwargs)
#         return inner
#     return wrapper
#
#
# @decorator('python')  # 等价于 func3 = decorator('python')(func3)，调用时需要传入参数
# def func3():
#     print("python ！！！")
#
# func3()
