Little Weaver's Wagtail-powered website.

Development
=============

Prerequisites
-------------

The installation instructions below assume you have the following software on your machine:

* `Python 2.7.x <http://www.python.org/download/releases/2.7.6/>`_
* `Pip <https://pip.readthedocs.org/en/latest/installing.html>`_
* `virtualenv <http://www.virtualenv.org/en/latest/virtualenv.html#installation>`_ (optional)
* `virtualenvwrapper <http://virtualenvwrapper.readthedocs.org/en/latest/install.html>`_ (optional)
* `PostgreSQL <http://www.postgresql.org/>`_

Installation instructions
-------------------------

Clone the Git repository from ``https://github.com/littleweaver/littleweaverweb.com.git``.

Make sure to ``cd littleweaverweb.com`` into the repo directory before following the next steps.

Python dependencies
+++++++++++++++++++

If you are using virtualenv or virtualenvwrapper, create and activate an environment. E.g.,

.. code:: bash

    mkvirtualenv lww                   # Using virtualenvwrapper.

Then install the requirements:

.. code:: bash

    pip install -r requirements.txt

Node dependencies
+++++++++++++++++

Install node dependencies.

.. code:: bash

    npm install -g postcss-cli autoprefixer

Database initialization
+++++++++++++++++++++++

The first time you run, you'll need to run migrations and create a superuser:

.. code:: bash

    python manage.py migrate           # Create/sync the database.
    python manage.py createsuperuser   # Create an initial user.

Get it running
--------------

If you are using virtualenv and RVM, ensure that you are on the appropriate virtual environment, gemset, and ruby version. E.g.,

.. code:: bash

    workon lww                         # Switch virtualenv.
    python manage.py runserver         # Run the server!

Then, navigate to ``http://127.0.0.1:8000/`` in your favorite web browser to view the site! Navigate to ``http://127.0.0.1:8000/admin/`` to edit pages.
