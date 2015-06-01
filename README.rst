Little Weaver's Wagtail-powered website.

Naming
======

The name of this software is django-brambling. The name for use within the content of the application and for marketing purposes is Dancerfly.

Development
=============

Prerequisites
-------------

The installation instructions below assume you have the following software on your machine:

* `Python 2.7.x <http://www.python.org/download/releases/2.7.6/>`_
* `Ruby 2.2.1 <https://www.ruby-lang.org/en/installation/>`_
* `RVM <https://rvm.io/>`_
* `Pip <https://pip.readthedocs.org/en/latest/installing.html>`_
* `virtualenv <http://www.virtualenv.org/en/latest/virtualenv.html#installation>`_ (optional)
* `virtualenvwrapper <http://virtualenvwrapper.readthedocs.org/en/latest/install.html>`_ (optional)

Installation instructions
-------------------------

Clone the Git repository from ``https://github.com/littleweaver/littleweaverweb.com.git``.

If you are using virtualenv or virtualenvwrapper, create and activate an environment. E.g.,

.. code:: bash

    mkvirtualenv brambling # Using virtualenvwrapper.

If you are using RVM, make sure to create an use an appropriate gemset with Ruby 2.2.1. If you are not using RVM, you must set environment variable ``GEM_PATH`` to a colon-separated list of locations where gems are found.

Get it running
--------------

.. code:: bash

    cd django-brambling/test_project
    python manage.py migrate           # Create/sync the database.
    python manage.py createsuperuser   # Create an initial user.
    python manage.py runserver         # Run the server!

Then, navigate to ``http://127.0.0.1:8000/`` in your favorite web browser!
