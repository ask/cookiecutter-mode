# -*- coding: utf-8 -*-
"""{{ cookiecutter.project_short_description }}"""
# :copyright: (c) {{ cookiecutter.year }}, {{ cookiecutter.full_name }}
#             All rights reserved.
# :license:   BSD (3 Clause), see LICENSE for more details.
import re
import sys
import typing
from typing import Any, Mapping, NamedTuple, Sequence

__version__ = '{{ cookiecutter.version }}'
__author__ = '{{ cookiecutter.full_name }}'
__contact__ = '{{ cookiecutter.email }}'
__homepage__ = 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}'
__docformat__ = 'restructuredtext'

# -eof meta-


class version_info_t(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: str
    serial: str


# bumpversion can only search for {current_version}
# so we have to parse the version here.
_match = re.match(r'(\d+)\.(\d+).(\d+)(.+)?', __version__)
if _match is None:
    raise RuntimeError('{{ cookiecutter.project_slug }} VERSION HAS ILLEGAL FORMAT')
_temp = _match.groups()
VERSION = version_info = version_info_t(
    int(_temp[0]), int(_temp[1]), int(_temp[2]), _temp[3] or '', '')
del(_match)
del(_temp)
del(re)


# Import stuff here
# from {{ cookiecutter.project_slug }} import Foo

__all__ = [
    #'Foo',
]
