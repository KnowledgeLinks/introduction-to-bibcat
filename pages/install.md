author: http://orcid.org/0000-0002-7543-3893
category: bc-qs
date: 2017-10-30
next: importing-bibcat
previous: quickstart
title: Installing BIBCAT

## Dependencies
*  [Python 3.6][PY36]

## Create a Python Virtual Environment
The recommended way to use BIBCAT is to first create a Python 
[Virtual Environment](https://docs.python.org/3/library/venv.html) 
to install [BIBCAT][BC] and all of it's module dependencies.

1.  Create a new Python virtual environment

    <pre><code>
    $ python3 -m venv /path/bibcat-env
    </code></pre>

1.  Activate `bibcat-env` virtual environment

    <pre><code>
    $ source /path/bibcat-env/bin/activate
    (bibcat-env) $
    </code></pre>


## Using PIP
With the `bibcat-env` active, you'll can install [BIBCAT][BC] from
[PyPI][PYPI], the Python Package Index, with the following:

<pre><code>
(bibcat-env) $ pip install bibcat
</code></pre>

## From Source code

1.  Use [git]() to clone a copy of the [BIBCAT][BC] from Github and
    then go into the directory.

    <pre><code>
    $ git clone https://github.com/KnowledgeLinks/bibcat.git
    $ cd bibcat
    </code></pre>

1.  **OPTION 1 (recommended)** - Install [BIBCAT][BC] with PIP using 
    the `-e` flag to allow editing of BIBCAT code in your installed
    Python (system or virtual environment):

    <pre><code>
    (bibcat-env) $ pip install -e .
    </code></pre>

1.  **OPTION 2** - Install [BIBCAT][BC] using `setup.py`:

    <pre><code>
    $ python3 setup.py install
    </code></pre>
    
[BC]: https://github.com/KnowledgeLinks/bibcat
[PY36]: https://www.python.org/downloads/release/python-363/
[PYPI]: https://pypi.python.org/pypi
