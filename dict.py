# -*- coding: utf-8 -*-

class MyDictUsingDict(dict):
    # def __repr__(self):
    #     return repr(self.__dict__)

    # def __len__(self):
    #     return len(self.__dict__)

    # def __delitem__(self, key):
    #     del self.__dict__[key]

    # def clear(self):
    #     return self.__dict__.clear()

    # def copy(self):
    #     return self.__dict__.copy()

    # def has_key(self, k):
    #     return self.__dict__.has_key(k)

    # def pop(self, k, d=None):
    #     return self.__dict__.pop(k, d)

    # def update(self, *args, **kwargs):
    #     return self.__dict__.update(*args, **kwargs)

    # def keys(self):
    #     return self.__dict__.keys()

    # def values(self):
    #     return self.__dict__.values()

    # def items(self):
    #     return self.__dict__.items()

    # def pop(self, *args):
    #     return self.__dict__.pop(*args)

    # def __cmp__(self, dict):
    #     return cmp(self.__dict__, dict)

    # def __contains__(self, item):
    #     return item in self.__dict__

    # def __iter__(self):
    #     return iter(self.__dict__)

    # def __unicode__(self):
    #     return unicode(repr(self.__dict__))
    def __setitem__(self, key, item):
        self.data[key] = item

    def __getitem__(self, key):
        return self.data[key]
    # assignment will be after the right values
    __getattr__ = __getitem__
    __setattr__ = __setitem__

class MyDict(object):
    def __init__(self, *args, **kwargs):
    	# will call the __setattr__ method
    	self.data = {}
    	if not kwargs:
    		self.data.update(kwargs)

    def __setitem__(self, key, item):
        self.data[key] = item

    def __getitem__(self, key):
        return self.data[key]

    # def __getattr__(self, key):
    # 	return self.data[key]
    # same method using assignment
    __getattr__ = __getitem__

    def __setattr__(self, key, val):
    	if key == 'data':
    		super(MyDict, self).__setattr__(key, val)
    	else:
    		# will not call the __setattr__, but __setitem__ of dict
    		self.data[key] = val

import unittest
class TestAttrDict(unittest.TestCase):

    def setUp(self):
    	# test Mydict class
        self.AttrDict = MyDict

    def test_get_item(self):
        my_dict = self.AttrDict()
        my_dict.test = 123
        self.assertEquals(my_dict.test, 123)
        self.assertEquals(my_dict['test'], 123)

    def test_set_item(self):
        my_dict = self.AttrDict()
        my_dict['test'] = 123
        self.assertEquals(my_dict['test'], 123)
        self.assertEquals(my_dict.test, 123)

# dict in python
def syntax_dict():
    val = {}
    # pop the key which not exit without exception
    # val.pop(key, None)
    val.pop(1, None)
    val.setdefault(1, []).extends(range(10))

    # constructor
    tuples = zip(range(5), range(5))
    val = dict(tuples)
    lists = map(lambda x:list(x), zip(range(5), range(5)))
    val = dict(lists)

if __name__ == '__main__':
	unittest.main()
