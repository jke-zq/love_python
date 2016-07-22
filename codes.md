#####1.lambda: nested defaultdict
~~~python
import collections
nested_map = collections.defaultdict(lambda :collections.defaultdict(int))
#usage: nested_map[key][nested_key] += 1
~~~

####2.zip and dict
~~~python
dict(zip(listkey, listval))
# init dict
# mapping
dict(key1='val1', key2='val2')
# kv
dict(**kw)
# iterator
dict([('key1', 'val1'), ('key2', 'val2')])
# init defaultdict
defaultdict(default_factor, other_paramters_same_with_dict)
~~~

####3.current dir and path
~~~python
import os
# the directory of the script being run
os.path.dirname(os.path.abspath(__file__))
# the current working directory
os.getcwd(
~~~

####4.reload moudle in python interpreter
~~~shell
>>import imp
>>imp.reload(moudle)
~~~

####5. nerver use import *
##### what happend:
* for package: everyting in "__init__.py"
* for moudle: everyting in moudel.py && "__all__"

##### why not:
* Because it puts a lot of stuff into your namespace (might shadow some other object from previous import and you won't know about it).
* Because you don't know exactly what is imported and can't find place from what module certain thing was imported easily (readability).
* Because you can't use cool tools like pyflakes to detect statically errors in your code.

####6. from package.moudle import func or import package.moudle
######todo

####7. rsplit vs split(from left)
~~~shell
>>'3#4#5'.rsplit('#')
['3', '4', '5']
>>'3#4#5'.rsplit('#', -1)
['3', '4', '5']
>>'3#4#5'.rsplit('#', 1)
['3#4', '5']
>>'3#4#5'.rsplit('#', 2)
['3', '4', '5']
>>'3#4#5'.split('#', 1)
['3', '4#5']
~~~

####8. read lines from file and remove the \n in the end of the line
~~~python
for line in f.readlines(): # not good, maybe files with too many lines
	line = line.strip('\n')
~~~
