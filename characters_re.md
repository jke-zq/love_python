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

####3.4-byte char raises MySQL erro:"Incorrect string value"
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