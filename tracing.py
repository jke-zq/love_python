# -*- coding: utf-8 -*-
__author__ = 'zhaoqing'

# read from URL:https://pymotw.com/2/sys/tracing.html

import sys


def trace_calls(frame, event, arg):
    if event != 'call':
        return
    co = frame.f_code
    func_name = co.co_name
    if func_name == 'write':
        # Ignore write() calls from print statements
        return
    func_line_no = frame.f_lineno
    func_filename = co.co_filename
    caller = frame.f_back
    caller_line_no = caller.f_lineno
    caller_filename = caller.f_code.co_filename
    print 'Call to %s on line %s of %s from line %s of %s' % \
        (func_name, func_line_no, func_filename,
         caller_line_no, caller_filename)
    return


def call_b():
    print 'in call_b()'


def call_a():
    print 'in call_a()'
    call_b()

# sys.settrace(trace_calls)

def trace_explict_lines(frame, event, arg):
    if event != 'line':
        return
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    filename = co.co_filename
    print '  %s line %s' % (func_name, line_no)

def trace_lines_calls(frame, event, arg):
    if event != 'call':
        return
    co = frame.f_code
    func_name = co.co_name
    if func_name == 'write':
        # Ignore write() calls from print statements
        return
    line_no = frame.f_lineno
    filename = co.co_filename
    print 'Call to %s on line %s of %s' % (func_name, line_no, filename)
    if func_name in TRACE_INTO:
        # Trace into this function
        return trace_explict_lines
    return

def line_c(input):
    print 'input =', input
    print 'Leaving line_c()'

def line_b(arg):
    val = arg * 5
    line_c(val)
    print 'Leaving line_b()'

def line_a():
    line_b(2)
    print 'Leaving line_a()'

TRACE_INTO = ['line_b']

# sys.settrace(trace_lines_calls)


def trace_calls_and_returns(frame, event, arg):
    co = frame.f_code
    func_name = co.co_name
    if func_name == 'write':
        # Ignore write() calls from print statements
        return
    line_no = frame.f_lineno
    filename = co.co_filename
    if event == 'call':
        print 'Call to %s on line %s of %s' % (func_name, line_no, filename)
        return trace_calls_and_returns
    elif event == 'return':
        print '%s => %s' % (func_name, arg)
    return


def return_b():
    print 'in return_b()'
    return 'response_from_b '


def return_a():
    print 'in return_a()'
    val = return_b()
    return val * 2

# sys.settrace(trace_calls_and_returns)

def trace_exceptions(frame, event, arg):
    if event != 'exception':
        return
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    filename = co.co_filename
    exc_type, exc_value, exc_traceback = arg
    print 'Tracing exception: %s "%s" on line %s of %s' % \
        (exc_type.__name__, exc_value, line_no, func_name)

def trace_exceptions_calls(frame, event, arg):
    if event != 'call':
        return
    co = frame.f_code
    func_name = co.co_name
    if func_name in TRACE_INTO:
        return trace_exceptions

def exception_c():
    raise RuntimeError('generating exception in c()')

def exception_b():
    exception_c()
    print 'Leaving exception_b()'

def exception_a():
    exception_b()
    print 'Leaving exception_a()'

TRACE_INTO = ['exception_a', 'exception_b', 'exception_c']

sys.settrace(trace_exceptions_calls)

if __name__ == '__main__':
    # Tracing Function Calls
    # call_a()
    # Tracing Inside Functions
    # line_a()
    # Watching the Stack
    # return_a()
    # Exception Propagation
    # exception_a()
    # or
    try:
        exception_a()
    except Exception, e:
        print 'Exception handler:', e