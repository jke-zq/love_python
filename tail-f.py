def coroutine(func):
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        cr.next()
        return cr
    return start

import time
def follow(the_files, target):
    for file in the_files:
        file.seek(0, 2) # Go to the end of the file
    try:
        while True:
            for file in the_files:
                line = file.readline()
                if not line:
                    time.sleep(0.1) # Sleep briefly
                    continue
                target.send(file.name + ':' + line)
                # raise Exception('invalid follow...')
    except Exception as e:
        raise

@coroutine
def printer():
    try:
        print 'init printer...'
        while True:
            line = (yield)
            print line
            # raise Exception('invalid printer...')
    except Exception as e:
        print 'printer except...'
        raise

if __name__ == '__main__':
    try:
        access = open('access-log')
        error = open('error-log')
        # not printer, it should printer() to run the printer func
        follow((access, error), printer())
    except Exception as e:
        ## catch exceptions from printer() and follow()
        print 'enter into except...'
        raise
    finally:
        print 'enter into finally...'
        access.close()
        error.close()

