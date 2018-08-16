=====================================================================
 {{ cookiecutter.project_name }}: {{ cookiecutter.project_short_description }}
=====================================================================

|build-status| |license| |wheel| |pyversion| |pyimp|

.. include:: ../includes/introduction.txt

.. include:: ../includes/installation.txt

.. include:: ../includes/code-of-conduct.txt

.. |build-status| image:: https://secure.travis-ci.org/{{ cookiecutter.github_repo }}.png?branch=master
    :alt: Build status
    :target: https://travis-ci.org/{{ cookiecutter.github_repo }}

.. |license| image:: https://img.shields.io/pypi/l/{{ cookiecutter.project_slug }}.svg
    :alt: BSD License
    :target: https://opensource.org/licenses/BSD-3-Clause

.. |wheel| image:: https://img.shields.io/pypi/wheel/{{ cookiecutter.project_slug }}.svg
    :alt: {{ cookiecutter.project_name }} can be installed via wheel
    :target: http://pypi.python.org/pypi/{{ cookiecutter.project_slug }}

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg
    :alt: Supported Python versions.
    :target: http://pypi.python.org/pypi/{{ cookiecutter.project_slug }}/

.. |pyimp| image:: https://img.shields.io/pypi/implementation/{{ cookiecutter.project_slug }}.svg
    :alt: Supported Python implementations.
    :target: http://pypi.python.org/pypi/{{ cookiecutter.project_slug }}/
