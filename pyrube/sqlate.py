#!/usr/bin/env python
"""sqlate.py
"""

from __future__ import print_function
import functools
import inspect
import sqlite3
import types


def executor(func, *args):

    assert not isinstance(func, types.BuiltinFunctionType)

    with sqlite3.connect(':memory:') as conn:
        nargs = len(inspect.getargspec(func).args)
        conn.create_function('rubewrapper', nargs, func)

        cur = conn.cursor()

        fmt = ','.join(['?']*nargs)
        cur.execute('SELECT rubewrapper({})'.format(fmt), args)
        res = cur.fetchone()

        return res[0]


def sqlate(func):
    @functools.wraps(func)
    def new_func(*args):
        return executor(func, *args)
    return new_func


if __name__ == '__main__':
    def main():
        import time

        def sleep(seconds):
            return time.sleep(seconds)

        print('sleep(.5) =', executor(sleep, .5))

        import operator

        @sqlate
        def death_adder(x, y):
            return operator.add(x, y)

        print('operator.add(1, 2) =', death_adder(1, 2))

    main()
