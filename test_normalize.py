import unittest

from normalize import normalize_label


class NormalizeLabelTest(unittest.TestCase):
    def test_spaces_and_case(self):
        self.assertEqual(normalize_label("  Example  "), "example")

    def test_empty_label(self):
        self.assertEqual(normalize_label(""), "")
