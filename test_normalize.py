import unittest

from normalize import normalize_label


class NormalizeLabelTest(unittest.TestCase):
    def test_spaces_and_case(self):
        self.assertEqual(normalize_label("  Example  "), "example")

    def test_collapses_repeated_internal_whitespace(self):
        self.assertEqual(normalize_label(" \tExample  \tLABEL\t "), "example label")
