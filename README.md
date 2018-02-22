blogpostpy
===============================

version number: 0.0.1
author: Max Resnick

Overview
--------

a simple blogpost api

* stays true to the given schema - no changes
* no adding features like auth, OWASP etc but also dont go and run `eval`
* no walking large sets of data e.g `/posts`
* that _easily_ installable is a working modernish python environment not Ansible/Puppet or even Docker.


Installation / Usage
--------------------
Installation requirements:

    1. Working pip installation on a modern version of python3+ (this should work with python2 but is untested).
    2. Pip should be also be recent version

To install use pip:

    $ pip install git+https://github.com/grumps/blogpostpy

Or clone the repo:

    $ git clone https://github.com/grumps/blogpostpy.git
    $ python setup.py install

Usage:

    Running the server

    $ gunicorn blogpostpy:app

    Getting blog posts

    $ curl 127.0.0.1:8000/posts | python -m json.tool

    Adding blog posts

    $ curl -H "Content-Type: application/json" -X POST -d '{"title":"foo","body":"bar"}' 127.0.0.1:8000/post

Contributing
------------

TBD

Example
-------

TBD
