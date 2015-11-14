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
```python
#!/usr/bin/env python

print("This is python-101")
``` 
There are two ways to run this file:
* `python foo.py`
* Make it executable `chmod +x foo.py` and run the executable `./foo.py`

### Introduction to Python

#### Numbers
##### +, -, * and /

These operator works similar to other languages. 
```python
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # division always returns a floating point number
1.6
```

* `/` always returns a float.
* `//` can be used to discard the fractional part
* `%` can be used to calculate the remainder
* `**` is used to calculate powers
* `=` is used to assign a value to a variable

```python
>>> 12 ** 2
144
>>> 2 ** 3
8 
```

##### Variable assignment:

```python
>>> a = 12
>>> b = 14
>>> a + b
26
>>> c = a + b
>>> c
26

```

In interactive mode the last printed expression is assigned to a variable named `_`

#### Strings

* Strings can be enclosed in single quotes (`'...'`)or double quotes(`"..."`).
* `\` Can be used for escaped quotes
* We can use a combination of single quotes and double quotes to avoid use of `\` before escaped character

```python
>>> 'This is BangPypers'
'This is BangPypers'
>>> 'Rama don\'t like python'
'Rama don't like python'
>>> "Hari don't know why"
"Hari don't know why"
```
* `print()` function omits the enclosing quotes.

```python
>>> print("Hari loves python")
Hari loves python

```
* If you want to print the string as it is without interpreting prefaced `\` as a special character then use raw strings 

```python
>>> print('home\abc')
homebc
>>> print(r'home\abc')
home\abc
```

* If string is too long use triple quotes, `("""...""" or '''...''')`

```python
>>> print(""" Python is very easy
... I am learning python 
... It is a beautiful language """)
Python is very easy
I am learning python 
It is a beautiful language 
>>> 
``` 
* Strings can be concatenated using `+` and repeated with `*`

```python
>>> "p" + "y" * 5 + "thon"
'pyyyyython'

```
* Two or more string literals, next to each other are automatically concatenated.
* To concatenate a string literal and a string variable we must use `+`

```python
>>> "hello" "world"
'helloworld'
>>> var = "abc"
>>> var + "def" 
'abcdef'
>>> var "def"  # This will give syntax error
File "<stdin>", line 1
var "def"
^
SyntaxError: invalid syntax

```

##### String Indexing

* First character of a string has index 0
* Character is a string of size 1
* If index is a negative number, it starts counting form the right
* Negative indices start form -1

```python
>>> word = "This is Python Bangpypers"
>>> word[0]  # Indexing starts from 0
'T'
>>> word[1]
'h'
>>> word[5]
'i'
>>> word[12]
'o'
>>> word[-1] # -ve indexing starts form -1 and it points to last character
's'
>>> word[-2]
'r'
>>> word[-5]
'y'
>>> 

```

* To obtain substring we use word slicing
* In `word[2:10]`, character at index `2` is included and at index `10` is excluded
* Slices have default indices. An omitted first index defaults to `0` and omitted 2nd index defaults to size of the string

```python
>>> word[15:-1]   # -ve index also works in slicing 
'Bangpyper'
>>> word[15:]     # last index defaults to length of the string
'Bangpypers'
>>> word[1:]        
'his is Python Bangpypers'
>>> word[:]       # First index defaults to 0
'This is Python Bangpypers'
>>> word[0:5]      
'This '

```

* Python strings are immutable 

```python
>>> word[5] = 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

```

##### String Methods
* `capitalize()`: Return a copy of the string with its first character capitalized and the rest lowercased
* `center(width[, fillchar])`: Return centered in a string of length width
* `count(sub[, start[, end]])`: Return the number of non-overlapping occurrences of substring sub in the range [start, end]
* `find(sub[, start[, end]])`: Return the lowest index in the string where substring sub is found
* `format()`: Returns a copy of the string where each replacement field is replaced with the string value of the corresponding argument.

```python
>>> "The sum of 1 + 2 is {0}".format(1+2)
'The sum of 1 + 2 is 3'
``` 
* `isalnum()`: Returns true if the string is alphanumeric
* `isalpha()`, `isdecimal()`,`isdigit()`, or `isnumeric()`
* `join()`: Return a string which is the concatenation of the strings, passed as argument in join. 

```python
#!/usr/bin/python

s = "-";
seq = ("a", "b", "c"); # This is sequence of strings.
print s.join( seq )
```
* `split`: The method split() returns a list of all the words in the string, using str as the separator optionally limiting the number of splits to num.

```python
#!/usr/bin/python

str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split( )
print str.split(' ', 1 )

output:

['Line1-abcdef', 'Line2-abc', 'Line4-abcd']
['Line1-abcdef', '\nLine2-abc \nLine4-abcd']
```
* There are many other predefined methods for strings, see [here](https://docs.python.org/3/library/stdtypes.html#string-methods)

##### String Formating printf-style
See the examples below

```python
>>> print("My name is %s, I am %d yrs old" %("rajiv", 15))   # As tuples 
My name is rajiv, I am 15 yrs old
>>> print('%(language)s has %(number)03d quote types.' %     # As dictionary
...       {'language': "Python", "number": 2})
Python has 002 quote types.
```

##### in and len()
* `len(str)`: This will return the length of the string, `str`
* `"abc" in str`: Will return `true` if "abc" is substring of `str`

`str` is a string variable

### Data Structures

#### Lists

* Comma separated values between square brackets
* Lists can also be indexed and sliced
* List also support concatenation by `+`
* Lists are mutable
* To add items at the end of the list use `append()`

```python
>>> list = [1, 2, 3, 4, 5, 6]
>>> list
[1, 2, 3, 4, 5, 6]
>>> list[0]                        # indexing returns the item
1
>>> list[4]                        # indexing returns the item
5
>>> list[-1]                        # indexing returns the item
6

>>> list[2:]                        # Slicing returns a new list
[3, 4, 5, 6]

>>> list + [12, 13, 14]             # list support concatenation
[1, 2, 3, 4, 5, 6, 12, 13, 14]

>>> list[4] = 1000                  # lists are mutable
>>> list
[1, 2, 3, 4, 1000, 6]

>>> list.append("Bangalore")        # Will append bangalore at the end of the list
>>> list
[1, 2, 3, 4, 1000, 6, 'Bangalore']

>>> list[2:4] = ["Python"]          # Slices can also be initialized
>>> list                            
[1, 2, 'Python', 1000, 6, 'Bangalore']

>>> len(list)                       # length of list can be found using len 
6


>>> ### Nesting of list
... 
>>> 
>>> a = [1, 2, 3]
>>> b = ["m", "n", "o"]
>>> nlist = [a, b]
>>> nlist
[[1, 2, 3], ['m', 'n', 'o']]
>>> nlist[0]
[1, 2, 3]
>>> nlist[1]
['m', 'n', 'o']
>>> nlist[1][0]
'm'
>>> nlist[0][2]
3


```

#### Tuples

#### Dictionaries



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
