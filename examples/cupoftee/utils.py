# -*- coding: utf-8 -*-
"""
    cupoftee.utils
    ~~~~~~~~~~~~~~

    Various utilities.

    :copyright: (c) 2009 by the Werkzeug Team, see AUTHORS for more details.
    :license: BSD, see LICENSE for more details.
"""
import re


_sort_re = re.compile(r'\w+', re.UNICODE)


def unicodecmp(a, b):
    x, y = map(_sort_re.search, [a, b])
    return cmp((x.group() if x else a).lower(), (y.group() if y else b).lower())
