# -*- coding: utf-8  -*-
#
# Copyright (C) 2012 Ben Kurtovic <ben.kurtovic@verizon.net>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from mwparserfromhell.nodes import Node

__all__ = ["Template"]

class Template(Node):
    def __init__(self, name, params=None):
        self._name = name
        if params:
            self._params = params
        else:
            self._params = []

    def __unicode__(self):
        if self.params:
            params = u"|".join([unicode(param) for param in self.params])
            return "{{" + unicode(self.name) + "|" + params + "}}"
        else:
            return "{{" + unicode(self.name) + "}}"

    @property
    def name(self):
        return self._name

    @property
    def params(self):
        return self._params

    def has_param(self):
        pass

    def get_param(self):
        pass

    def add_param(self):
        pass

    def remove_param(self):
        pass