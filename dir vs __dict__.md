First of all, dir() is a API method that knows how to use attributes like ____dict\_\___ to look up attributes of an object.

***1.Not all objects have a ____dict\_\___ attribute though.*** 

For example, if you were to add a ____slots\_\___ attribute to your custom class, instances of that class won't have a ____dict\_\___ attribute, yet dir()can still list the available attributes on those instances:

~~~shell
>>> class Foo(object):
...     __slots__ = ('bar',)
...     bar = 'spam'...
>>> Foo().__dict__
Traceback (most recent call last):File "<stdin>", line 1, in <module>AttributeError: 'Foo' object has no attribute '__dict__'
>>> dir(Foo())
['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', 'bar']
~~~
**For Example**
The same applies to many built-in types; lists do not have a ____dict\_\___ attribute, but you can still list all the attributes using dir():

~~~shell
>>> [].__dict__
Traceback (most recent call last):File "<stdin>", line 1, in <module>AttributeError: 'list' object has no attribute '__dict__'
>>> dir([])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
~~~
***2.What dir() does with instances
Python instances have their own ____dict\_\___, but so does their class:***

~~~shell
>>> class Foo(object):
...     bar = 'spam'
...
>>> Foo().__dict__
{}
>>> Foo.__dict__.items()
[('__dict__', <attribute '__dict__' of 'Foo' objects>), ('__weakref__', <attribute '__weakref__' of 'Foo' objects>), ('__module__', '__main__'), ('bar', 'spam'), ('__doc__', None)]
>>> >>> dir(Foo())
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'bar']
~~~
***3.The dir() method uses both these ____dict\_\___ attributes, and the one on object to create a complete list of available attributes on the instance, the class, and on all ancestors of the class.***

When you set attributes on a class, instances see these too:

~~~shell
>>> f = Foo()
>>> f.ham
Traceback (most recent call last):File "<stdin>", line 1, in <module>AttributeError: 'Foo' object has no attribute 'ham'
>>> Foo.ham = 'eggs'
>>> f.ham
'eggs'
~~~
because the attribute is added to the class ____dict\_\___:

~~~shell
>>> Foo.__dict__['ham']
'eggs'
>>> f.__dict__
{}
~~~
Note how the instance ____dict\_\___ is left empty. Attribute lookup on Python objects follows the hierarchy of objects from instance to type to parent classes to search for attributes.

****4.Only when you set attributes directly on the instance, will you see the attribute reflected in the ____dict\_\___ of the instance, while the class ____dict\_\___ is left unchanged:***

~~~shell
>>> f.stack = 'overflow'
>>> f.__dict__
{'stack': 'overflow'}
>>> 'stack' in Foo.__dict__
False
~~~
***TLDR; or the summary***

dir() doesn't just look up an object's ____dict\_\___ (which sometimes doesn't even exist), it will use the object's heritage (its class or type, and any superclasses, or parents, of that class or type) to give you a complete picture of all available attributes.

An instance ____dict\_\___ is just the 'local' set of attributes on that instance or class, and does not contain every attribute available on the class. Instead, you need to look at the class and the class's inheritance tree too.

getmembers() does not return metaclass attributes when the argument is a class (this behavior is inherited from the dir() function).