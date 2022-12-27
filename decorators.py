def f1():
    print(f" Executing function f1.")
f1()
print(f1)
print(type(f1))
def f2 (func):
    func()
f2(f1)
x_func=f1
f2(x_func)
def f3(func):
    def wrapper():
        print(f" About to start executing func.")
        func()
        print(f" Finished executing func.")
    return wrapper
#@f3
def hello_world():
    print(f"Hello World ")
#hello_world()
f3(hello_world)
def hello_world1():
    print(f"Hello world one !")
hello_world1()
def f3_copy(func):
    def wrapper():
        print(f" About to Start executing func .")
        func()
        print(f" finished Executing func.")
    wrapper()
f3_copy(hello_world1)
def f4 (func):
    def wrapper(*args,**kwargs):
        print(f" About to execute function: {func.__name__}")
        func(*args,**kwargs)
        print(f" Finisided exceuting function :{func.__name__}")
    return wrapper
@f4
def do_add(x,y):
    print(f"sum of {x} {y} : {x+y}")
do_add(10,20)
do_add('Hello', 'World')
