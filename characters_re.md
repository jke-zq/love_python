####1. isalpha in string or unicode
* in string: use str.isalpha() to check if str only contains letters
* in unicode: unicode.isalpha() is to check if it only contains characters in LETTER part.
* using re to check if unicode only contains letters.

~~~python
import re
if re.match(r'[a-zA-Z]+$', data) is None:
	print 'data doesnt only contain letters'
~~~

####2. check the password
##### 1).consist of lowercase, uppercase, digit, punctuation without space
##### 2).should not just consist of one from the four kinds
##### 3).length: 6 ~ 20
~~~~python
import re
PASSWORD_REG = re.compile('[\x21-\x7E]{6,20}$')

def has_lowercase(pw):
    return len(set(string.ascii_lowercase).intersection(pw)) > 0


def has_uppercase(pw):
    return len(set(string.ascii_uppercase).intersection(pw)) > 0


def has_numeric(pw):
    return len(set(string.digits).intersection(pw)) > 0


def has_special(pw):
    return len(set(string.punctuation).intersection(pw)) > 0


def get_kinds_chars(pw):
    checkers = [has_lowercase, has_uppercase, has_numeric, has_special]
    kinds = reduce(lambda x, check_func: x + 1 if check_func(pw) else x, checkers, 0)
    return kinds
    
# other way --start
def intersect(collection, pw):
    return set(collection).intersection(pw)


def get_count_intersections(collects, pw):
    count = reduce(lambda x, coll: x + 1 if len(intersect(coll, pw) > 0 else x, collects, 0)
    return count
# other way --end    
    
if __name__ == '__main__':
    if not PASSWORD_REG.match(value) or get_kinds_chars(value) < 2:
        raise Exception('{} is not a valid password string'.format(value))
    print 'valid password'
~~~~

####3. print \x21 - \x7E
~~~shell
>>b'\x21'
'!'
~~~

~~~python
def hex2str(chain):
	chars = (chr(int(chain[i:i+2], 16)) for i in range(0, len(chain), 2))
	print type(chars)
    return ''.join(chars)
# usage: hex2str('232425')    output: '#$%'
~~~
#####REF URL:
* [Conversion functions between binary, hexadecimal and ASCII](http://codereview.stackexchange.com/questions/85079/conversion-functions-between-binary-hexadecimal-and-ascii)
* [Validate Password Complexity](https://www.safaribooksonline.com/library/view/regular-expressions-cookbook/9781449327453/ch04s19.html)

####4.4-byte char raises MySQL erro:"Incorrect string value"
[Warning raised by inserting 4-byte unicode to mysql](http://stackoverflow.com/questions/10798605/warning-raised-by-inserting-4-byte-unicode-to-mysql)

If MySQL cannot handle UTF-8 codes of 4 bytes or more then you'll have to filter out all unicode characters over codepoint \U00010000; UTF-8 encodes codepoints below that threshold in 3 bytes or fewer.
You could use a regular expression for that:

~~~shell
>> import re
>> highpoints = re.compile(u'[\U00010000-\U0010ffff]')
>> example = u'Some example text with a sleepy face: \U0001f62a'
>> highpoints.sub(u'', example)
u'Some example text with a sleepy face: '
~~~
Alternatively, you could use the .translate() function with a mapping table that only contains None values:

~~~shell
>> nohigh = { i: None for i in xrange(0x10000, 0x110000) }
>> example.translate(nohigh)
u'Some example text with a sleepy face: '
~~~
However, creating the translation table will eat a lot of memory and take some time to generate; it is probably not worth your effort as the regular expression approach is more efficient.

This all presumes you are using a UCS-4 compiled python. If your python was compiled with UCS-2 support then you can only use codepoints up to '\U0000ffff' in regular expressions and you'll never run into this problem in the first place.

I note that as of MySQL 5.5.3 the newly-added utf8mb4 codec does supports the full Unicode range.
[Python, convert 4-byte char to avoid MySQL error “Incorrect string value:”](http://stackoverflow.com/questions/12636489/python-convert-4-byte-char-to-avoid-mysql-error-incorrect-string-value)

In a UCS-2 build, python uses 2 bytes internally for each unicode character over \U0000ffff code point. Regular expressions need to work with those, so you'd need to use the following regular expression to match these:

~~~python
highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
~~~
This regular expression matches any 2-byte UTF-16-encoded code point (see UTF-16 Code points U+10000 to U+10FFFF.

To make this compatible across Python UCS-2 and UCS-4 versions, you could use a try:/except to use one or the other:

~~~python
import re
try:
    # UCS-4
    highpoints = re.compile(u'[\U00010000-\U0010ffff]')
except re.error:
    # UCS-2
    highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
~~~
Qing ZHao: if your python is using UCS-4, you can "list(unicode)" or "for u in unicode". But if your python is using UCS-2, you can split one 4-bytes unicode into two 2-bytes unicodes.

####5. str vs unicode
[Python str vs unicode types](http://stackoverflow.com/questions/18034272/python-str-vs-unicode-types)

unicode, which is python 3's str, is meant to handle text. Text is a sequence of code points which may be bigger than a single byte. Text can be encoded in a specific encoding to represent the text as raw bytes(e.g. utf-8, latin-1...). Note that unicode is not encoded! The internal representation used by python is an implementation detail, and you shouldn't care about it as long as it is able to represent the code points you want.

On the contrary str is a plain sequence of bytes. It does not represent text! In fact, in python 3 str is called bytes.

You can think of unicode as a general representation of some text, which can be encoded in many different ways into a sequence of binary data represented via str.

Some differences that you can see:

~~~shell
>>> len(u'à')  # a single code point
1
>>> len('à')   # by default utf-8 -> takes two bytes
2
>>> len(u'à'.encode('utf-8'))
2
>>> len(u'à'.encode('latin1'))  # in latin1 it takes one byte
1
>>> print u'à'.encode('utf-8')  # terminal encoding is utf-8
à
>>> print u'à'.encode('latin1') # it cannot understand the latin1 byte
�
~~~
Note that using str you have a lower-level control on the single bytes of a specific encoding representation, while using unicode you can only control at the code-point level. For example you can do:

~~~shell
>>> 'àèìòù'
'\xc3\xa0\xc3\xa8\xc3\xac\xc3\xb2\xc3\xb9'
>>> print 'àèìòù'.replace('\xa8', '')
à�ìòù
~~~
What before was valid UTF-8, isn't anymore. Using a unicode string you cannot operate in such a way that the resulting string isn't valid unicode text. You can remove a code point, replace a code point with a different code point etc. but you cannot mess with the internal representation.
 When you want to save some text(e.g. to a file) you have to represent it with bytes, i.e. you must encode it. When retrieving the content you should know the encoding that was used, in order to be able to decode the bytes into a unicode object.

NEED TO BE READ:
[Screwing up Python compatibility: unicode(), str(), and bytes()](http://blog.labix.org/2009/07/02/screwing-up-python-compatibility-unicode-str-bytes)

####6. "__str__" vs "__unicode__"
[Python __str__ versus __unicode__](http://stackoverflow.com/questions/1307014/python-str-versus-unicode)

"__str__()" is the old method -- it returns bytes. "__unicode__()" is the new, preferred method -- it returns characters. The names are a bit confusing, but in 2.x we're stuck with them for compatibility reasons. Generally, you should put all your string formatting in "__unicode__()", and create a stub "__str__()" method:

~~~python
def __str__(self):
    return unicode(self).encode('utf-8')
~~~
In 3.0, str contains characters, so the same methods are named "__bytes__()" and "__str__()". These behave as expected.