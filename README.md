<p align="center"><img src="artwork/manbearpig.png"></p>

<p align="center">
  <b>manbearpig</b> is a *super-serial* python application structure / layout example.
</p>

## TL;DR
```
/{{ project }}
|-- bin
|   -- runnable_something
|-- docs
|   -- ??
|-- {{ project }}
|   -- __init__.py
|   -- something.py
|   -- submodule
|      -- __init__.py
|-- tests
|   -- __init__.py
|   -- context.py
|   -- test_something.py
|-- Makefile
|-- LICENSE.txt
|-- README.md
|-- requirements-dev.txt
|-- requirements.txt
`-- setup.py
```

Find this runnable structure under [{{ project }}](/%7B%7B%20project%20%7D%7D).

### {{ project }}/bin

Project executables go here :grimacing:


## {{ project }}/{{ project }}

Your reusable source code lives here.

## {{ project }}/tests

Your tests live here :fire:

## {{ project }}/Makefile

Handy shortcuts to get stuff done :smile_cat: for example:

```
install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

test:
	py.test tests
```

You could then do: `$ make test` to run your tests.

## {{ project }}/LICENSE.txt

Lawyer up! Checkout [choosealicense.com](https://choosealicense.com/) as a handy starting point.

## {{ project }}/README.md

You're reading one now. Hopefully I don't have to explain how useful they are :coffee:

## {{ project }}/requirements-dev.txt

All your dev requirements, try to version them when you can.

## {{ project }}/requirements.txt

All your application requirements, again, try to version them when you can.

Handy tip: `$ pip freeze > requirements.txt`

## {{ project }}/setup.py

Your setup file if you need one.

## Inspired By

* http://docs.python-guide.org/en/latest/writing/structure/
* https://coderwall.com/p/lt2kew/python-creating-your-project-structure
* http://www.patricksoftwareblog.com/structure-of-a-python-project/
