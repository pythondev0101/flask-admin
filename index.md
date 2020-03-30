# HomeBest Framework
An application framework written in Flask

## Features

* Preconfigured setup for [Travis CI](https://travis-ci.org/), [Coveralls](https://coveralls.io/), and [Scrutinizer](https://scrutinizer-ci.com/)
* `pyproject.toml` for managing dependencies and package metadata
* `Makefile` for automating common [development tasks](https://github.com/jacebrowning/template-python/blob/master/%7B%7Bcookiecutter.project_name%7D%7D/CONTRIBUTING.md):
    - Installing dependencies with `poetry`
    - Automatic formatting with `isort` and `black`
    - Static analysis with `pylint`
    - Type checking with `mypy`
    - Docstring styling with `pydocstyle`
    - Running tests with `pytest`
    - Building documentation with `mkdocs`
    - Publishing to PyPI using `poetry`
* Tooling to launch an IPython session with automatic reloading enabled

If you are instead looking for a [Python application](https://caremad.io/posts/2013/07/setup-vs-requirement/) template, check out one of the sibling projects:

* [jacebrowning/template-django](https://github.com/jacebrowning/template-django)
* [jacebrowning/template-flask](https://github.com/jacebrowning/template-flask)

## Examples

Here are a few sample projects based on this template:

* [jacebrowning/minilog](https://github.com/jacebrowning/minilog)
* [theovoss/Chess](https://github.com/theovoss/Chess)
* [sprout42/StarStruct](https://github.com/sprout42/StarStruct)
* [MichiganLabs/flask-gcm](https://github.com/MichiganLabs/flask-gcm)
* [flask-restful/flask-restful](https://github.com/flask-restful/flask-restful)

## Usage

Install `cookiecutter` and generate a project:

```
$ pip install cookiecutter
$ cookiecutter gh:jacebrowning/template-python -f
```

Cookiecutter will ask you for some basic info (your name, project name, python package name, etc.) and generate a base Python project for you.

If you still need to use legacy Python or `nose` as the test runner, older versions of this template are available on branches:

```
$ cookiecutter gh:jacebrowning/template-python -f --checkout=python2

$ cookiecutter gh:jacebrowning/template-python -f --checkout=nose
```

## Updates

Run the update tool, which is generated inside each project:

```
$ bin/update
```
