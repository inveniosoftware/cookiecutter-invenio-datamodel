{% include 'misc/header.rst' %}

Installation
============

{{cookiecutter.project_name}} is on PyPI so all you need is:

.. code-block:: console

    $ pip install {{ cookiecutter.project_shortname }}

Normally, your instance will specify the correct dependency on your database
and Elasticsearch version you use. If not, you can explict install the
dependencies via the following extra install targets:

- ``elasticsearch5``
- ``elasticsearch6``
- ``postgresql``
- ``mysql``

For instance:

.. code-block:: console

    $ pip install {{ cookiecutter.project_shortname }}[postgresql,elasticsearch6]
