import {{ cookiecutter.project_slug }}


def test_dir():
    assert dir({{ cookiecutter.project_slug }})
    assert '__version__' in dir({{ cookiecutter.project_slug }})
