.. _etgen.usage:

=====
Usage
=====


.. currentmodule:: etgen.html

The :mod:`etgen.html` module defines an ElementTree Builder for generating HTML
documents.

.. data:: E

    The global ElementTree Builder object.

Usage:

>>> from etgen.html import E, tostring, tostring_pretty, CLASS, fromstring
>>> import lxml.usedoctest
>>> html = E.html(
...            E.head( E.title("Hello World") ),
...            E.body(
...              E.h1("Hello World !"),
...              CLASS("main")
...            )
...        )

>>> print (tostring_pretty(html))
<html>
  <head>
    <title>Hello World</title>
  </head>
  <body class="main">
    <h1>Hello World !</h1>
  </body>
</html>


>>> kw = dict(title='Ein süßes Beispiel')
>>> kw.update(href="foo/bar.html")
>>> btn = E.button(type='button', **CLASS('x-btn-text x-tbar-upload'))
>>> html = E.a(btn, **kw)
>>> print (tostring_pretty(html))
<a href="foo/bar.html" title="Ein süßes Beispiel">
  <button class="x-btn-text x-tbar-upload" type="button"/>
</a>

You can also do the opposite, i.e. parse HTML using
:func:`lxml.etree.fromstring`:

>>> html = fromstring('''<a href="foo/bar.html"
... title="Ein s&#252;&#223;es Beispiel">
... <button class="x-btn-text x-tbar-upload" type="button"/>
... </a>''')
>>> print(tostring_pretty(html))
<a href="foo/bar.html" title="Ein süßes Beispiel">
  <button class="x-btn-text x-tbar-upload" type="button"/>
</a>


>>> print(tostring(fromstring(
...     '<ul type="disc"><li>First</li><li>Second</li></ul>')))
<ul type="disc"><li>First</li><li>Second</li></ul>

>>> html = E.div(E.p("First"), E.p("Second"))
>>> print(tostring_pretty(html))
<div>
  <p>First</p>
  <p>Second</p>
</div>
>>> html.attrib['class'] = 'htmlText'
>>> print(tostring_pretty(html))
<div class="htmlText">
  <p>First</p>
  <p>Second</p>
</div>

Avoid self-closing tags
=======================

lxml generates self-closing tags for elements without children:

>>> print(tostring(E.div()))
<div/>

Some environments refuse empty ``<div>`` elements and interpret a ``<div/>`` as
``<div>`` (don't ask me why).  You can avoid the self-closing tag by setting
the ``text`` attribute to an empty string:

>>> html = E.div()
>>> html.text = ""
>>> print(tostring(html))
<div></div>

Note that you must set ``text`` explicitly. Simply specifying it when
instantiating the element is not enough:

>>> print(tostring(E.div("")))
<div/>

>>> print(tostring(E.div(" ")))
<div/>

The real solution would be to use the "html" method when writing the tree to
html:

>>> print(tostring(E.div(), method="html"))
<div></div>

TODO: This approach has been active as default value (see disabled line in code
of :func:`tostring`) and I don't remember why we disabled it.  I suggest to
re-enable it and test thoroughly whether this causes regressions (and if yes,
why it causes them).


Converting text lines to a paragraph
====================================

The :func:`lines2p` function  convert list of text lines into a paragraph
(``<p>``) with one ``<br>`` between each line.  If optional `min_height` is
given, add empty lines if necessary.

Examples:

>>> from etgen.html import lines2p

>>> print(tostring(lines2p(['first', 'second'])))
<p>first<br/>second</p>

>>> print(tostring(lines2p(['first', 'second'], min_height=5)))
<p>first<br/>second<br/><br/><br/></p>

If `min_height` is specified, and `lines` contains more items,
then we don't truncate:

>>> print(tostring(lines2p(['a', 'b', 'c', 'd', 'e'], min_height=4)))
<p>a<br/>b<br/>c<br/>d<br/>e</p>

This also works:

>>> print(tostring(lines2p([], min_height=5)))
<p><br/><br/><br/><br/></p>



Background
==========

The following code still works but is deprecated because :mod:`lxml` does it
better.

>>> from etgen.utils import Namespace

>>> E = Namespace('http://my.ns',
...    "bar baz bar-o-baz foo-bar class def".split())

>>> bob = E.bar_o_baz()
>>> baz = E.add_child(bob, 'baz', class_='first')
>>> print(E.tostring(baz))
<baz xmlns="http://my.ns" class="first" />

>>> bob = E.bar_o_baz('Hello', class_='first', foo_bar="3")
>>> print(E.tostring(bob))
<bar-o-baz xmlns="http://my.ns" class="first" foo-bar="3">Hello</bar-o-baz>

The following reproduces a pifall. Here is the initial code:

>>> E = Namespace(None, "div br".split())
>>> bob = E.div("a", E.br(), "b", E. br(), "c", E.br(), "d")
>>> print(E.tostring(bob))
<div>a<br />b<br />c<br />d</div>

The idea is to use :func:`join_elems` to insert the <br> tags:

>>> from etgen.utils import join_elems

But surprise:

>>> elems = join_elems(["a", "b", "c", "d"], sep=E.br())
>>> print(E.tostring(E.div(*elems)))
<div>a<br />bcd<br />bcd<br />bcd</div>

What happened here is that the same `<br>` element instance was being
inserted multiple times at different places.  The correct usage is
without the parentheses so that `join_elems` instantiates each time a
new element:

>>> elems = join_elems(["a", "b", "c", "d"], sep=E.br)
>>> print(E.tostring(E.div(*elems)))
<div>a<br />b<br />c<br />d</div>
