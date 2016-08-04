# pyrube

A python module in tribute to [Rube Goldberg](https://en.wikipedia.org/wiki/Rube_Goldberg).

## Installation

Just copy module directory anywhere you want. Just show some respect to Mr. Rube and
don't just use cp/copy -- use something more complicated.

## Getting Started

The module is ready to use. Just import it.

### sqlate

A handy wrapper to call your favorite functions via sqlite function.

```python
from pyrube.sqlate import sqlate

@sqlate
def catatonia(seconds):
    import time
    time.sleep(seconds)

catatonia(1.5)
```

```python
>>> from pyrube.sqlate import sqlate
>>>
>>> @sqlate
... def death_adder(x, y):
...     import operator
...     return operator.add(x, y)
>>>
>>> death_adder(1, 3)
4
>>>
```

## Getting Help

If you need help installing or using the module, you shouldn't.
