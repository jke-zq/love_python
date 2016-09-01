#### 1.Generator
~~~shell
>>a = (i * i for i in range(10))
<generator object <genexpr> at 0x102632550>
~~~

#### 2.List
~~~shell
>>a = [i * i for i in range(10)]
>># tuple to list
>>list(tuple_val)
~~~

####3.Controlling a generator exhaustion
~~~shell
>>> class Bank(): # let's create a bank, building ATMs
...    crisis = False
...    def create_atm(self):
...        while not self.crisis:
...            yield "$100"
>>> hsbc = Bank() # when everything's ok the ATM gives you as much as you want
>>> corner_street_atm = hsbc.create_atm()
>>> print(corner_street_atm.next())
$100
>>> print(corner_street_atm.next())
$100
>>> print([corner_street_atm.next() for cash in range(5)])
['$100', '$100', '$100', '$100', '$100']
>>> hsbc.crisis = True # crisis is coming, no more money!
>>> print(corner_street_atm.next())
<type 'exceptions.StopIteration'>
>>> wall_street_atm = hsbc.create_atm() # it's even true for new ATMs
>>> print(wall_street_atm.next())
<type 'exceptions.StopIteration'>
>>> hsbc.crisis = False # trouble is, even post-crisis the ATM remains empty
>>> print(corner_street_atm.next())
<type 'exceptions.StopIteration'>
>>> brand_new_atm = hsbc.create_atm() # build a new one to get back in business
>>> for cash in brand_new_atm:
...    print cash
$100
$100
$100
~~~
#### 4.Itertools