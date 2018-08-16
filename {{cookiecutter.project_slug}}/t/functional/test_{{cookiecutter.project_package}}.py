import {{ cookiecutter.project_package }}


def test_dir():
    assert dir({{ cookiecutter.project_package }})
    assert '__version__' in dir({{ cookiecutter.project_package }})
