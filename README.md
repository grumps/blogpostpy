blogpostpy
===============================

version number: 0.0.2
author: Max Resnick

Overview
--------

a simple blogpost api

* stays true to the given schema - no changes
* no adding features like auth, OWASP etc but also dont go and run `eval`
* no walking large sets of data e.g `/posts`
* that _easily_ installable is a working modernish python environment not Ansible/Puppet or even Docker.
* installs tested Debian Sid and Debian 9


Installation / Usage
--------------------
Installation requirements:

    1. Working pip installation on a modern version of python3+ (this should work with python2 but is untested).
    2. Pip should be also be recent version
    3. You are installing in a virtual environment (python) console scripts tends to be bit weird for system packages

Install with all dependencies

    $ wget https://github.com/grumps/blogpostpy/releases/download/v0.0.2/blogpostpy-0.0.2-py2.py3-none-any.whl
    $ pip install blogpostpy-0.0.2-py2.py3-none-any.whl

To install use pip:

    $ pip install git+https://github.com/grumps/blogpostpy

Or clone the repo:

    $ git clone https://github.com/grumps/blogpostpy.git
    $ python setup.py install


Contributing
------------

TBD

Example
-------

Usage:                                                                                                       
                                                                                                             
    Running the server                                                                                       
                                                                                                             
    $ gunicorn blogpostpy:app                                                                                
                                                                                                             
    Getting blog posts                                                                                       
                                                                                                             
    $ curl 127.0.0.1:8000/posts | python -m json.tool                                                        
                                                                                                             
    Adding blog posts                                                                                        
                                                                                                             
    $ curl -H "Content-Type: application/json" -X POST -d '{"title":"foo","body":"bar"}' 127.0.0.1:8000/post 
                                                                                                             
