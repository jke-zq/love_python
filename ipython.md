####1.Shell Command
* use shell command in Ipython like in shell.
* assign the result of the shell command to a python variable.

~~~
#in fact: files = get_ipython().getoutput(u'ls')
In [12]: files = !ls

In [13]: type(files)
Out[13]: IPython.utils.text.SList
~~~
####2.Running .py File
file foo.py in the present working directory can be executed using run

~~~shell
>> %run file.py
~~~
####3.Timing Code
~~~shell
>>#
>>%time func
>>#
>>%timeit func
~~~

####4.Reloading Modules
Note: The imported py files will be complied into byte code files, in preparation for seding its instructions to the python virtual machine. The byte code files will be called pyc files, and live in the same directory of the py files.
Even though we've modified the imported py files, this change will not reflected in pyc files.
The nicest way to get your dependencies to recomplie is to use Ipython's autoreload extension.

* load automatically when you start IPython, add these lines to your ipython_config.py file

~~~
c.InteractiveShellApp.extensions = ['autoreload']
c.InteractiveShellApp.exec_lines = ['%autoreload 2']
~~~

* do things manually, you can also import and then reload the modified module

~~~shell
>>import useful_functions
>>reload(useful_functions)
~~~

####5.Debugging
me:I use print results and ctrl+b in sumblime ->_->.

####6.Others
* precision 4 sets printed precision for floats to 4 decimal places
* whos gives a list of variables and their values
* quickref gives a list of magics

####7.Getting Help
ends with "?" to show docstr.
####8.Edit

* %edit
* %edit -p

####9.Save commands to file
This is will save the specific lines to a given file. You can pass any number of arguments separated by space.

~~~
In [9]: %save hello.py 1-2 2-3
File `hello.py` exists. Overwrite (y/[N])?
Operation cancelled.
~~~
####10.Recall
~~~
# type this
In [7]: %recall 2

# auto convert this, you can enter ctrl to execute it.
In [8]: datetime.datetime.now()
~~~
####11.history
~~~
In [14]: history 4
type(a)

# Line from 4 and 7(included) in the current session
In [15]: history 4-7
type(a)
%save 1-2 2-3
%save hello.py 1-2 2-3
%recall 2
# Line 4 in the last session.
In [19]: history ~1/4
ls

#option: "-op" -- to execute the history lines
In [3]: history 1
datetime

In [4]: history -op 1
>>> datetime
<module 'datetime' from '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/datetime.so'>
~~~
####12.Out
~~~ipython
# print last output
In [17]: print _
# print last last output
In [18]: print __
# print the output with the line number
In [19]: print _1
# all output marked with "Out[index]:" will stroed in Out(dict:index->value)
In [20]: print Out
~~~
####13.Logging Session
~~~
In [29]: log
%logoff    %logon     %logstart  %logstate  %logstop

In [29]: %logstart
Activating auto-logging. Current session state plus future input saved.
Filename       : ipython_log.py
Mode           : rotate
Output logging : False
Raw input log  : False
Timestamping   : False
State          : active

# You can use ipython_log to start the Ipython.
zhaoqing@onePiece ~/o/my_leetcode> ipython -i ipython_log.py
~~~
####14.pastbin
~~~
In [5]: pastebin 3-4
Out[5]: u'https://gist.github.com/498bf5804bfe1ba9d1bc2128c0ee8428'
~~~
REF:

* [Quantitative Economics](http://quant-econ.net/py/ipython.html)
* [End Point](http://blog.endpoint.com/2015/06/ipython-tips-and-tricks.html)
* [Speaker Deck](https://speakerdeck.com/zsiciarz/ipython-tips-tricks-magic)