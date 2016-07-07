__author__ = 'zhaoqing'

# nested defaultdict
import collections
nested_map = collections.defaultdict(lambda :collections.defaultdict(int))
# ex: nested_map[key][nested_key] += 1
