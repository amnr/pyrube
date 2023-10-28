#!/usr/bin/env python3
"""A handy wrapper to call your favorite functions via sqlite function."""

import sqlite3
from functools import wraps
from inspect import getfullargspec
from types import BuiltinFunctionType


def executor(func, *args):
    """Run function with arguments via sqlite."""
    if isinstance(func, BuiltinFunctionType):
        raise TypeError('Builtin functions are not supported')

    with sqlite3.connect(':memory:') as conn:
        nargs = len(getfullargspec(func).args)
        conn.create_function('rubewrapper', nargs, func)

        cur = conn.cursor()

        fmt = ','.join(['?'] * nargs)
        cur.execute(f'SELECT rubewrapper({fmt})', args)
        res = cur.fetchone()

        return res[0]


def sqlate(func):
    """Run decorator."""
    @wraps(func)
    def new_func(*args):
        return executor(func, *args)
    return new_func


if __name__ == '__main__':
    import operator
    import time

    def main():
        """Main."""

        def sleep(seconds):
            return time.sleep(seconds)

        print('sleep(2.5) =', executor(sleep, 2.5))

        @sqlate
        def death_adder(xval, yval):
            return operator.add(xval, yval)

        print('operator.add(1, 2) =', death_adder(1, 2))

    main()

# vim: set sts=4 et sw=4:
