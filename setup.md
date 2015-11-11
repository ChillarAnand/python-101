## Installation instructions

We will be using Python 3.5 for the workshop.


### Ubuntu

If you are using ubuntu, python will be installed by default. With Ubuntu 14.04, you will get `python 3.4`.

Lets install `python 3.5`.

Open a terminal by pressing `CTRL + ALT + T`.

Execute the following commands.

```sh
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get install python3.5
```

Type `python3.5` and press enter, you should see something like this


```sh
$ python3.5
Python 3.5.0 (default, Sep 17 2015, 00:00:00)
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```


### Mac

- To install any developer tools in OS X, [XCode Command Line Tools](http://osxdaily.com/2014/02/12/install-command-line-tools-mac-os-x/) are mandatory.

- [brew](http://brew.sh/) is extremely popular package manager in OS X.
`brew` is similar to `apt-get` or `yum` in GNU/Linux operating system.

- `brew install python3`. This will install latest Python version ie. Python 3.5.

- Type `python3.5` in terminal or shell.

```python
➜  ~  python3.5
Python 3.5.0 (default, Sep 23 2015, 04:42:00)
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.72)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

- If you don't like to use any package manager, download official [python package](https://www.python.org/ftp/python/3.5.0/python-3.5.0-macosx10.6.pkg).


### Windows
