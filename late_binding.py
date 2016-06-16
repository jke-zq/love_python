def multipliers():
    return [lambda x : i * x for i in range(4)]

print [m(2) for m in multipliers()]


#在闭包中的变量是在内部函数被调用的时候被查找。所以结果是，当任何 multipliers() 返回的函数被调用，在那时，i 的值是在它被调用时的周围作用域中查找
# using default arg
def multipliers():
    return [lambda x, j=i : j * x for i in range(4)]

# using partial
from functools import partial
from operator import mul

def multipliers():
    # return [partial(lambda x, y: y * x, i) for i in range(4)]
    return [partial(mul, i) for i in range(4)]