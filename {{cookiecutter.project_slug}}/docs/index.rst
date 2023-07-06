Welcome to {{ cookiecutter.project_name }}'s documentation!
======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   readme
   installation
   usage
   design 
   modules
   contributing
   {% if cookiecutter.create_author_file == 'y' -%}authors
   {% endif -%}history

-----

Log Entries
==========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   log

-----
Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
