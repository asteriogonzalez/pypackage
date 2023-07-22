{{ cookiecutter.project_name }} Docs
=====================================================================

.. toctree::
   :maxdepth: 2

   readme
   installation
   usage
   design 
   modules
   contributing
   {% if cookiecutter.create_author_file == 'y' -%}authors
   {% endif -%}history



Log Entries
=====================================================================

.. toctree::
   :maxdepth: 2

   log

Indices and tables
=====================================================================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
