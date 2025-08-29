def logtime(func):
    def wrapper():
        print('before') # do something before
        val = func()
        print('after') # do something after
        return val
    return wrapper

@logtime
def hello():
    print('hello')

hello()