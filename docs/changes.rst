.. _etgen.changes: 

=======================
Changes in `etgen`
=======================

Version 0.0.5 (not released)
============================

Version 0.0.4 (released 2018-03-11)
====================================

- use the ElementTree builder (``E``) from :mod:`lxml` instead of my
  own implementation based on :mod:`xml.etree.ElementTree`. Though not
  the easy way. It has a few consequences (see below).

We cannot use `E.tostring()` any more because the ``E`` defined in
:mod:`lxml.etree` doesn't have that method.  My extended version of
:func:`tostring` is now as a global function in :mod:`etgen.html`.

Old code::

     from etgen.html import E
     ...
     E.tostring()

New code::
     
     from etgen.html import E, tostring
     ...
     tostring()

Same problem for `E.iselement` and `E.to_rst` and `E.raw`.

In lxml we don't have the hack of adding an underscore to attributes
like `class` which are a reserved in Python. We must convert these
cases.  Before::

  return E.li(a, class_="active")

After::

  return E.li(a, **{'class': "active"})

Failures saying `TypeError: bad argument type: __proxy__(u' by ')` are
because lxml elements don't like Django translatable strings.  Old
code::
  
    return E.div(E.h2(self.actor.label), e)
            
New code::
  
    return E.div(E.h2(str(self.actor.label)), e)

Another failure was in code which updates existing elements
:message:`TypeError: update() takes no keyword arguments`. Old code::
  
    e.attrib.update(align='right')
        
New code::

    e.set('align', 'right')




Version 0.0.3 (released 2018-02-16)
====================================

- Added a test case for :mod:`etgen.sepa.validate`.

- Added dependency to atelier (fix for
  https://travis-ci.org/lino-framework/etgen/jobs/342304371)

Version 0.0.2 (released 2018-02-16)
====================================

Added package data in :file:`etgen/sepa/XSD/*.xsd`.

Version 0.0.1 (released 2018-02-16)
====================================

The package was born as a repackaging of code which was previously in
Lino as the packages :mod:`lino.utils.xmlgen` and
:mod:`lino.utils.html2rst`.  We moved them out of Lino into an
independent package :mod:`etgen` because they might be of use also for
projects which don't use Lino.

