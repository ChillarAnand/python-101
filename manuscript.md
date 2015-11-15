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

A class is a specification (think of it as a blueprint or pattern and a set of instructions) 
of how to provide some service. 
Engineers and construction and factory workers use blueprints to build cars, buildings, bridges, 
virtually anything.  Tailors, seamsters, printers use patterns to make the clothes we wear, 
books we read.  Chefs follow recipes to put together meals.

```python
>>> class Maths:
    def sumof(self, x, y):
        return x+y
    def mulof(self, x, y):
        return x*y

>>> obj = Maths()
>>> obj.sumof(3,4)
7
>>> obj.mulof(3,4)
12
```

Common mistakes while coding during initial days
```
>>> class Maths:
    def sumof(x, y):
        return x+y
    def mulof(x, y):
        return x*y

>>> obj = Maths()
>>> obj.sumof(3,4)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    obj.sumof(3,4)
TypeError: sumof() takes 2 positional arguments but 3 were given
```

Below example from taken from
http://anandology.com/python-practice-book/object_oriented_programming.html#classes-and-objects
```python
class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

>>> a = BankAccount()
>>> b = BankAccount()
>>> a.deposit(100)
100
>>> b.deposit(50)
50
>>> b.withdraw(10)
40
>>> a.withdraw(10)
90

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
>>> obj = BankAccount(200)
>>> obj.balance
200
>>> obj.withdraw(50)
150
>>> obj.deposit(150)
300
```

Use docstring while writing code, that can be used to create documentation or while doing
help to the object

```python
>>> class BankAccount:
    """This class can be used to get the bank account details
       and also to do transaction.
    """
    def __init__(self, initial_balance=0):
        """Account holder can open their account with certail
           Initial balance, otherwise initial balace will be 0
        """
        self.balance = initial_balance

    def withdraw(self, amount):
        """This function can be used to withdraw amount from
           your account.
        """
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """This function can be used to deposit amount into
           your account.
        """
        self.balance += amount
        return self.balance

>>> help(BankAccount)
Help on class BankAccount in module __main__:

class BankAccount(builtins.object)
 |  This class can be used to get the bank account details
 |  and also to do transaction.
 |  
 |  Methods defined here:
 |  
 |  __init__(self, initial_balance=0)
 |      Account holder can open their account with certail
 |      Initial balance, otherwise initial balace will be 0
 |  
 |  deposit(self, amount)
 |      This function can be used to deposit amount into
 |      your account.
 |  
 |  withdraw(self, amount)
 |      This function can be used to withdraw amount from
 |      your account.
```

#### Inheritance
A language feature would not be worthy of the name “class” without supporting inheritance. 
The syntax for a derived class definition looks like this:

```Python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```
Example
```python
>> class Alto:
    def price(self):
        return '3L INR'
    def power(self):
        return '800cc'
    def maker(self):
        return 'Maruti'

>>> obj = Alto()
>>> obj.maker()
'Maruti'
>>> obj.power()
'800cc'
>>> 
>>> 
>>> class Swift(Alto):
    def new_features(self):
        return 'airbag, bluetooth'

>>> sw_obj = Swift()
>>> sw_obj.maker()
'Maruti'
>>> sw_obj.power()
'800cc'
>>> sw_obj.new_features()
'airbag, bluetooth'
>>> 
>>> class Swift_newgen(Swift):
    def price(self):
        return '5L INR'
    def power(self):
        return '1200cc'

>>> ng_obj = Swift_newgen()
>>> ng_obj.price()
'5L INR'
>>> ng_obj.power()
'1200cc'
>>> ng_obj.maker()
'Maruti'
>>> 
```
