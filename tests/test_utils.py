from pathlib import Path

from atelier.test import TestCase

import etgen

SRC = Path(etgen.__file__).parent


class UtilsTests(TestCase):

    # def test_init(self):
    #     self.run_simple_doctests(SRC + '__init__.py')

    def test_utils(self):
        self.run_simple_doctests(SRC / 'utils.py')

    def test_xmlgen_html(self):
        self.run_simple_doctests(SRC / 'html.py')

    def test_html2rst(self):
        self.run_simple_doctests(SRC / 'html2rst.py')

    def test_xmlgen_sepa(self):
        self.run_simple_doctests(SRC / 'sepa/__init__.py')
