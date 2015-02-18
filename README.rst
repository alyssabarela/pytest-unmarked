pytest-poo is a plugin for `pytest <http://pytest.org/>`_ that points out your
crappy tests with piles of poo.

Requirements
============
A recent version of pytest is required (>= 2.3.4).



Showing crappy (failed)  tests during test run
------------------------------------

Just run py.test with the ``--poo`` option to enable the output. To always
enable, add ``--poo`` to addopts in pytest.ini::

    [pytest]
    addopts = --poo


