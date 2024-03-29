#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2013-2018 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)
"""
"""

import sys
from lxml import etree

XSD_NAMESPACE = "http://www.w3.org/2001/XMLSchema"
XSD = "{%s}" % XSD_NAMESPACE

NSMAP = dict(xsd=XSD_NAMESPACE)


def xsdnames(fn, nsname):
    tree = etree.parse(fn)
    root = tree.getroot()
    names = set()

    def collect(e):
        na = e.get('name', None)
        if na is not None:
            names.add(na)
        for child in e:
            collect(child)

    collect(root)
    return ' '.join(names)


def main(fn):
    print(xsdnames(fn, 'ns0'))


if __name__ == "__main__":
    main(sys.argv[1])
