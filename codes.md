#####1.lambda: nested defaultdict
~~~python
import collections
nested_map = collections.defaultdict(lambda :collections.defaultdict(int))
#usage: nested_map[key][nested_key] += 1
~~~

