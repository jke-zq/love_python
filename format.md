#### 1. format
[PEP 3101 -- Advanced String Formatting](https://www.python.org/dev/peps/pep-3101/)

~~~shell
>> 'first parameter is {}, second parameter is {}'.format('first_param', 'second_param')
output:'first parameter is first_param, second parameter is second_param'
>> 'second parameter is {1}, first parameter is {0}'.format('first_param', 'second_param')
output:'second parameter is second_param, first parameter is first_param'
>> 'first parameter with key "name" is {0[name]}, first parameter with key "value" is {0[value]}'.format(dict(name='dict_name', value='dict_value'))
output:'first parameter with key "name" is dict_name, first parameter with key "value" is dict_value'
~~~

#### 2. %s
~~~python
s1, s2 = 's1', 's2'
ass = '%s:%s' %(s1, s2)
~~~