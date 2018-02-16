.. _etgen.changes: 

=======================
Changes in `etgen`
=======================

Version 0.0.4 (not released)
============================

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

