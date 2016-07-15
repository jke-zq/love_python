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
