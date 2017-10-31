## Python 2 Vs Python 3

Python 2.x is legacy.

Python 3.x is the present and future of the language


---------------------------------------------------------------------------

### Division

#### Python 2

```python
>>> 3 / 2
1
>>> 3 // 2
1
>>> 3 // float(2)
1.0
>>> 3 / 2 * 1.0
1.0
>>> 3 / (2 * 1.0)
1.5
```

#### Python 3

```python
>>> 3 / 2
1.5
>>> 3 // 2
1
>>> int(3 / 2)
1
```

---------------------------------------------------------------------------

### print

#### Python 2

`print` is a statement.

```python
>>> print('python')
python
>>> print x, y
1 2
>>> print(x, y)
(1, 2)
```

#### Python 3

`print` is a function.

```python
>>> print(x, y)
1 2
>>> print("hello")
hello
```

---------------------------------------------------------------------------

### unicode

#### Python 2

```python
>>> type('python')
<type 'str'>
>>> type(unicode('python'))
<type 'unicode'>
>>> type('python')
<type 'unicode'>

>>> print 'string \u03BC'
string \u03BC

```



#### Python 3

```python
>>> type('hello')
<class 'str'>
>>> type(u'hello')
<class 'str'>


>>> print('string \u03BC')
string μ

>>> r = 5
>>> π = 3.17
>>> c = 2 * π * r
>>> c
31.7
```

---------------------------------------------------------------------------

### range

#### Python 2

`range()` creates the list of integers in memory.

`xrange()` is an efficient way to produce integers without consuming a lot of memory.

```python
>>> x = range(20)
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> sys.getsizeof(x)
232
>>> y = xrange(20)
>>> y
xrange(20)
>>> sys.getsizeof(y)
40
```


#### Python 3

Has only `range()` which works like `xrange()`.

```python
>>> x = range(10)
>>> sys.getsizeof(x)
48
>>> xrange
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'xrange' is not defined
```

---------------------------------------------------------------------------


### classes

#### Python 2

Old style classes.

```python
class Account():
    pass
```

New style classes.

```python
class Account(object):
    pass
```

Can use descriptors.

Has  elegant `mro` for base class lookup.

Always use new style classes



#### Python 3

Only new style classes.


```python
class Account():
    pass
```

---------------------------------------------------------------------------

### iterators everywhere

#### Python 2

A lot of built-ins returned lists by default.

```
my_dict = {'name': 'Dan', 'age': 25}

>>> my_dict.keys()
['age', 'name']

>>> my_dict.items()
[('age', 25), ('name', 'Dan')]

>>> my_dict.values()
[25, 'Dan']
```

If you need iterators, you need to use iter* methods.

```
>>> my_dict.iterkeys()
<dictionary-keyiterator object at 0x207e050>

>>> my_dict.iteritems()
<dictionary-itemiterator object at 0x207e0a8>

>>> my_dict.itervalues()
<dictionary-valueiterator object at 0x207e158>
```


#### Python 3

Python 3 decided that it would be best to always return iterators for efficiency.


```
my_dict = {'name': 'Dan', 'age': 25}

>>> my_dict.keys()
dict_keys(['age', 'name'])

>>> my_dict.items()
dict_items([('age', 25), ('name', 'Dan')])

>>> my_dict.values()
dict_values([25, 'Dan'])

```

Other functions like `map()`, `filter()`, `range()`, `zip()` return iterators.

Also see: http://docs.python-guide.org/en/latest/writing/gotchas/
