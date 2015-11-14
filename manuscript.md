## Syllabus


### Using the Python Interpreter
#### Argument Passing
The python script name and additional arguments thereafter are turned into a list of string and assigned into argv variable in sys module.

* When no script and no argument:
	`sys.argv[0]` is an empty string
* When script name is given as -:
	`sys.argv[0]` is set to "-"
* When `-c` or `-m` command is used:
	`sys.argv[0]` is set to `-c` or `-m` respectively



`python -c 'print(hello world)'`

Here `-c` stands for a python command
Anything written after `-c` must be a valid python command

`python -m pdb python-101.py`

`-m` stands for module
`pdb` stands for python debugger
`python-101.py` is a file containing the python code

`python -i python-101.py`

`-i` means, python will run the program, `python-101.py` and dump you into 
interactive interpreter 
It helps in monitoring the variables at the end of the program.

To enter directly into python interpreter just type:
`python`

Another way using python interpreter: 
Create a file named foo.py

The content of the file foo.py:
```
#!/usr/bin/env python

print("This is python-101")
``` 
There are two ways to run this file:
* `python foo.py`
* Make it executable `chmod +x foo.py` and run the executable `./foo.py`

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

#### Function arguments

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


#### Builtin functions

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


>>> pow(3, 4)
81
```


Full list of functions can be [found here](https://docs.python.org/3.5/library/functions.html)

Lets try to understand `Lambda`.

Small anonymous functions can be created with the lambda keyword
```Python
def sumof(x,y):
    return x+y
```

Above function can also be represented using lambda
```python
lambda x,y: x+y
```

Lambda functions can be used wherever function objects are required. Said that, let us try some inbuilt 
functions like `map, filter`

As help help of map
```python
map(func, *iterables) --> map object
 |  
 |  Make an iterator that computes the function using arguments from
 |  each of the iterables.  Stops when the shortest iterable is exhausted.
```

we either can define a function first and then pass it as first param, or use lambda instead.
```python
map(sumof, [1,2,3], [4,5,6])
```
or 

```python
map(lambda x,y: x+y, [1,2,3], [4,5,6])
```

### File handling

Files can read/write using `open` function.

You should pass filename(string) as argument.

You can also pass mode(`'r'`, `'w'`), which is optional.

```
>>> f = open('data.txt')
>>> f
<open file 'data.txt', mode 'r' at 0x7fd3513d54b0>
>>> f = open('data.txt')
>>> for line in f:
...   print(line)
... 
If you are reading this using python,

You are on your way to become awesome python programmer.

Now that you have read the file,

try writing some text into a file.

>>>
```

Lets create and write something into a file.

```
>>> f = open('story.txt')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IOError: [Errno 2] No such file or directory: 'story.txt'
>>> f = open('story.txt', 'w')
>>> f.write('Once there lived a python programmer.')
>>> f.write('foo bar baz.')
>>> f.write('more foo')
>>> f.close()
```


### Classes
