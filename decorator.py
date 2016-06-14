import functools
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

if __name__ == '__main__':
    foo()
    print foo.__name__
    print foo.__doc__