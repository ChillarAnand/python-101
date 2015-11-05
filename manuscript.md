## Syllabus


### Using the Python Interpreter


### Introduction to Python

Numbers

Strings

### Data Structures

Lists

Tuples

Dictionaries



### Control Flow Tools

if Statements

for Statements


### Functions

#### Defining functions

Keyword `def` is used to create new  function.

```python
>>> def sum_n(n):
...     """ Prints sum of n natural numbers. """
...     print(n * (n + 1) / 2)
...
```

`def` is followed by function name `sum_n`, followed by arguements in parens `n`.

Statements followed by definition form body of function and they should be indented properly.

It can also have doc string to summarize what a function does. This is optional.

You can check whether an object is a function.

```python
>>> type(sum_n)
<class 'function'>
```

Calling a function with approriate arguements executes the function.

```python
>>> sum_n()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sum_n() missing 1 required positional argument: 'n'
>>> sum_n(5)
15.0
```

Functions are objects. They can be passed around just like variables.

```python
>>> add_n = sum_n
>>> add_n(5)
15.0
```


#### Return statement

Every function returns some value.

If user doesn't return any value, `None` will be returned.

```python
>>> x = sum_n(5)
15.0
>>> print(x)
None
```

Values can be returned from function using `return` statement.

We can modify previous function to return value instead of printing it.

```python
>>> def sum_n(n):
...     """ Returns sum of n natural numbers. """
...     return (n * (n + 1) / 2)
...
>>> x = sum_n(5)
>>> print(x)
15.0
```

### Function arguments

Arguements can be either positional or keyword.


```python
>>> def power(base, exponent):
...   return pow(base, exponent)
...
>>> power(2,  3)
8
>>> power(base=2, exponent=3)
8
```

Keyword arguements can be passed in any order.

```python
>>> power(exponent=3, base=2)
8
>>> power(base=2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  TypeError: power() missing 1 required positional argument: 'exponent'
```

We can assign default values to arguements to make them optional.

```python
>>> def power(base, exponent=1):
...     return  pow(base, exponent)
...
>>> power(2)
2
>>> power(2, 3)
8
>>> power(exponent=3, base=2)
8
```


### Builtin functions

Python has some builtin functions which are always available.


```python
>>> help()


>>> print('python')
python


>>> score = [45, 67,  89, -12]
>>> sum(score)
189
>>> len(score)
4
>>> max(score)
89
>>> min(score)
-12

>>> range(5)
range(0, 5)
>>> list(range(5))
[0, 1, 2, 3, 4]
```


Full list of functions can be [found here](https://docs.python.org/3.5/library/functions.html)



### File handling

### Classes
