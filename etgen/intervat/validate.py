# -*- coding: UTF-8 -*-
# Copyright 2012-2018 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)

USAGE = """
Usage:

  python -m etgen.intervat.validate SCHEMA XMLFILE

Arguments:

SCHEMA : the schema to validate against. Possible values are:

  id  internal name            French name
  --- ------------------------ --------------------------------
  clc ClientListingConsignment Liste des clients assujettis
  ico IntraConsignment         Liste des clients intracommunautaires
  --- ------------------------ --------------------------------
  
XMLFILE : the name of the xml file to validate, or '-' to read from stdin
"""

if __name__ == '__main__':

    import sys
    from lxml import etree
    from etgen import intervat

    if len(sys.argv) < 3:
        #~ raise Exception("Usage: python -m %s name of the file to be validated" % __name__)
        #~ raise Exception("Missing command-line argument: the name of the file to be validated.")
        print(USAGE)
        sys.exit(-1)
    nsname = sys.argv[1]
    fn = sys.argv[2]

    ns = getattr(intervat, nsname, None)
    if ns is None:
        print("Invalid type %r" % nsname)
        sys.exit(-1)

    doc = etree.parse(fn)
    ns.validate_doc(doc)
    print(fn, "is a valid %s" % ns.__class__.__name__)
