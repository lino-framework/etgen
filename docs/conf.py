# -*- coding: utf-8 -*-

extensions = []
from rstgen.sphinxconf import configure

configure(globals())

extensions += ['rstgen.sphinxconf.complex_tables']
extensions += ['sphinx.ext.autosummary']

import etgen

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['.templates']

# General information about the project.
project = "etgen"
copyright = '2002-2021 Rumma & Ko Ltd'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#

# The full version, including alpha/beta/rc tags.
#~ release = file(os.path.join(os.path.dirname(__file__),'..','VERSION')).read().strip()
release = etgen.__version__

# The short X.Y version.
version = '.'.join(release.split('.')[:2])
#~ version = lino.__version__

#~ print version, release

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = [
    'include',
]

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'sphinx'

# Options for HTML output
# -----------------------

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
# html_style = 'default.css'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = etgen.SETUP_INFO['name']

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#~ html_logo = 'logo.jpg'
#~ html_logo = 'lino-logo-2.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#~ html_favicon = 'favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['.static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'
#~ last_updated = True

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#~ html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**': ['globaltoc.html', 'searchbox.html', 'links.html'],
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#~ html_additional_pages = {
#~ '*': 'links.html',
#~ }

# If false, no module index is generated.
html_use_modindex = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, the reST sources are included in the HTML build as _sources/<name>.
html_copy_source = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''
html_use_opensearch = 'http://lino.saffre-rumma.net'

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'etgen'

# Options for LaTeX output
# ------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
#~ latex_documents = [
#~ ('index', 'lino.tex', ur'lino', ur'Luc Saffre', 'manual'),
#~ ]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

#language="de"

#~ show_source = True

#~ srcref_base_uri="http://code.google.com/lino"
#~ srcref_base_uri="http://code.google.com/p/lino/source/browse/#hg"

extlinks = {
    # 'djangoticket': ('http://code.djangoproject.com/ticket/%s', 'Django ticket #%s'),
    'srcref': (etgen.srcref_url, None),
}

autosummary_generate = True

#~ nitpicky = True # use -n in Makefile instead

# my_font_family = "Swiss, Helvetica, Nimbus"
# my_font_family = "Verdana, 'DejaVu Sans'"
# http://sphinx.pocoo.org/theming.html
# my_font_family = "Swiss, Helvetica, 'Liberation Sans'"
# html_theme_options = {
#     "font_family": my_font_family,
#     "head_font_family": my_font_family,
# }
# font_family: "'goudy old style', 'minion pro', 'bell mt', Georgia, 'Hiragino Mincho Pro', serif")

# html_theme = "default"
# html_theme_options = dict(
#     collapsiblesidebar=True,
#     externalrefs=True)

todo_include_todos = True

#~ New in version 1.1
gettext_compact = True

# extlinks.update(ticket=('https://jane.mylino.net/#/api/tickets/AllTickets/%s', '#'))

suppress_warnings = ['image.nonlocal_uri']
