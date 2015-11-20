## Python 2 Vs Python 3

Python 2.x is legacy.

Python 3.x is the present and future of the language


### Division

#### Python 2

```
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

```
>>> 3 / 2
1.5
>>> 3 // 2
1
>>> int(3 / 2)
1
```

### print

#### Python 2

`print` is a statement.

```
>>> print('python')
python
>>> print x, y
1 2
>>> print(x, y)
(1, 2)
```

#### Python 3

`print` is a function.

```
>>> print(x, y)
1 2
>>> print("hello")
hello
```

### range

#### Python 2

`range()` creates the list of integers in memory.

`xrange()` is an efficient way to produce integers without consuming a lot of memory.

```
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

```
>>> x = range(10)
>>> sys.getsizeof(x)
48
>>> xrange
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'xrange' is not defined
```


### range
#### Python 2
#### Python 3
