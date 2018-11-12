.. You should enable this project on travis-ci.org and coveralls.io to make
   these badges work. The necessary Travis and Coverage config files have been
   generated for you.

.. image:: https://travis-ci.org/zjiaksmc/ckanext-activitiestracker.svg?branch=master
    :target: https://travis-ci.org/zjiaksmc/ckanext-activitiestracker

.. image:: https://coveralls.io/repos/zjiaksmc/ckanext-activitiestracker/badge.svg
  :target: https://coveralls.io/r/zjiaksmc/ckanext-activitiestracker

.. image:: https://pypip.in/download/ckanext-activitiestracker/badge.svg
    :target: https://pypi.python.org/pypi//ckanext-activitiestracker/
    :alt: Downloads

.. image:: https://pypip.in/version/ckanext-activitiestracker/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-activitiestracker/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/ckanext-activitiestracker/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-activitiestracker/
    :alt: Supported Python versions

.. image:: https://pypip.in/status/ckanext-activitiestracker/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-activitiestracker/
    :alt: Development Status

.. image:: https://pypip.in/license/ckanext-activitiestracker/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-activitiestracker/
    :alt: License

=============
ckanext-activitiestracker
=============

.. Put a description of your extension here:
   What does it do? What features does it have?
   Consider including some screenshots or embedding a video!

Activities Tracker is a extension for tracking users' resource-level downloading activities in CKAN, and store the log details in Postgres DB locally.

This extension implemented a backend that provides a controller to let front-end developer to specify where they would like to track users' activities.

For example, to track resource download within <a> element.

<a class="btn btn-primary resource-url-analytics resource-type-{{ res.resource_type }}" href="{%  url_for 'get_resource_url', dataset_id=pkg.id, resource_id=res.id %}">
<i class="fa fa-arrow-circle-o-down"></i> {{ _('Download & Log') }}
</a>

------------
Requirements
------------

this extension requires ckanext-resourceauthorizer. https://github.com/etri-odp/ckanext-resourceauthorizer

This extension was developed and tested under CKAN >= 2.7.3

------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-activitiestracker:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-activitiestracker Python package into your virtual environment::

     cd /usr/lib/ckan/default/src/
     git clone https://github.com/Jiaza492/ckanext-activitiestracker.git
     python setup.py install

3. Add ``activitiestracker`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 restart


---------------
Config Settings
---------------

Run the following command to create the necessary tables in the database (ensuring the pyenv is activated)::

    (pyenv) $ paster --plugin=ckanext-activitiestracker activitiestracker initdb --config=/etc/ckan/default/production.ini

Run the following command to reindex the CKAN metadata in solr (ensuring the pyenv is activated)::

    (pyenv) $ paster --plugin=ckan search-index rebuild --config=/etc/ckan/default/production.ini

Finally, restart CKAN to have the changes take affect:

    sudo service apache2 restart


---------------------------------
Registering ckanext-activitiestracker on PyPI
---------------------------------

ckanext-activitiestracker should be availabe on PyPI as
https://pypi.python.org/pypi/ckanext-activitiestracker. If that link doesn't work, then
you can register the project on PyPI for the first time by following these
steps:

1. Create a source distribution of the project::

     python setup.py sdist

2. Register the project::

     python setup.py register

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the first release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.1 then do::

       git tag 0.0.1
       git push --tags

