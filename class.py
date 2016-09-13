# 1. access attr of a class
class Parent(object):
    val = 1
    values = [10]
class  Child1(Parent):
    pass
    # def __setattr__(self, key, val):
    #     print 'enter into __setattr__:', key, ' = ', val
    #     super(Child1, self).__setattr__(key, val)

class  Child2(Parent):
    pass

if __name__ == '__main__':
    # p = Parent()
    # p.val = 0:               #using __setattr__ to add member 'val' to p -- the instance of Parent class
    # p.values = 0:            #same as the one above
    # p.values[0] = 0:         #call the operation of the list from the Parent class, not call the __setattr__
    # p.values.append(1):      #same as the one above
    # Parent.values = 0        #directly to the member 'values' of the Parent class
    # Child2.values = 0        #set a new member of Child2 class and the instance of it will have the member

## note:
# Instances can access the member of the class and cant reset them using 'instance.val = newVal', but other instances have no effect. 
# But you can do some operations on them, if and only if the type of the member is mutable.
# Subclasses are the same.

# 2.getattr vs hasattr
# https://hynek.me/articles/hasattr/
# hasattr cant judge the property of an instance
# using getattr(instance, attr_name, default_val), without parameter:default_val, if attr_name is not the attr of the instance, Exception will be happended.
