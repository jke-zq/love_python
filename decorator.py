# -*- coding: utf-8 -*- 

import functools
#################################using function as decorator#####################
def simpleDecorator(f):
    @functools.wraps(f)
    def _wrapper(*args, **kw):
        print 'enter into f...'
        f(*args, **kw)
        print 'enter out f...'
    return _wrapper

def argsDecorator(*arg):
    def _decorFun(f):
        @functools.wraps(f)
        def _wrapper(*args, **kw):
            f(*args, **kw)
            print arg
        return _wrapper
    return _decorFun

def commDecorator(*args):
    def _decoFun(f):
        @functools.wraps(f)
        def _wrapper(*args, **kw):
            print before
            f(*args, **kw)
            print after
        return _wrapper
    # need to init 'before' and 'after'
    if len(args) == 1 and callable(args[0]):
        # args[0] is function
        before, after = "before", "after"
        return _decoFun(args[0])
    else:
        # args are the values in '()'
        if len(args) == 1:
            before, after = args[0], args[0]
        else:
            before, after = "before", "after"
        return _decoFun

# @simpleDecorator
# @argsDecorator("arg")
# @commDecorator()
# @commDecorator
@commDecorator('haha')
def foo():
    for __ in range(1000000):
        pass

######################################using class as decorator#############################
class DecoratorClass(object):
 
    def __init__(self, fn):
        self.fn = fn
 
    def __call__(self):
        self.fn()
 
class DecoratorClassWithArgs(object):

    def __init__(self, args):
        self.args = args

    def __call__(self, func):
        def _wrapper(*args, **kw):
            print self.args
            func(*args, **kw)
        return _wrapper
         

@DecoratorClassWithArgs('args')
# @DecoratorClass
def fooFun():
    print 'fooFun with decorator class'
fooFun()

####################################decorate a class###################################
import inspect

def log(func):
    def wrapped(*args, **kwargs):
        try:
            print "Entering: [%s] with parameters %s" % (func.__name__, args)
            try:
                return func(*args, **kwargs)
            except Exception, e:
                print 'Exception in %s : %s' % (func.__name__, e)
        finally:
            print "Exiting: [%s]" % func.__name__
    return wrapped

def trace(cls):
    for name, m in inspect.getmembers(cls, inspect.ismethod):
        setattr(cls,name,log(m))
    return cls

#@trace(log)
# class trace(object):

#     def __init__(self, f):
#         self.f = f

#     def __call__(self, cls):
#         for name, m in inspect.getmembers(cls, inspect.ismethod):
#             setattr(cls, name, self.f(m))
#         return cls


@trace
class X(object):

    def first_x_method(self):
        print 'doing first_x_method stuff...'

    def second_x_method(self):
        print 'doing second_x_method stuff...'
################################some notes########################
## more @ 
# @decorator_one
# @decorator_two
# def func():
#     pass
# 相当于：
# func = decorator_one(decorator_two(func))

## more args
# @decorator(arg1, arg2)
# def func():
#     pass
# 相当于：
# func = decorator(arg1,arg2)(func)

if __name__ == '__main__':
    foo()
    print foo.__name__
    print foo.__doc__