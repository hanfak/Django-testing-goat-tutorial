# Additional stuff to get it working

## Before:

Create virtual environment, and install django and selenium as per book instructions

## Chapter 1.1

Need to download gecko driver for firefox to run with selenium. This needs to be unzipped and moved to /usr/local/bin, use CLI `mv <file> /usr/local/bin`

https://github.com/SeleniumHQ/selenium/blob/master/py/docs/source/index.rst

To create project, `django-admin startproject superlists`

To leave virtual environment `deactivate`

## Chapter 1.2

## Chapter 1.3

`AttributeError: module 'html.parser' has no attribute 'HTMLParseError'`

occurs, then upgrade django `pip install -U django`

Upgrade selenium

## Chapter 1.4

add `print(repr(html))` in test method to get what is printed out, for debugging

Use functional tests to drive html content in templates

## Chapter 1.5

```
import time
time.sleep(10)
```

Place in functional tests to stop browser and see what is happening
