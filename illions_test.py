import unittest

from illions import get_illion_prefix, format_illions


class IllionsTest(unittest.TestCase):
    def test_prefixes(self):
        self.assertEqual("m", get_illion_prefix(1))
        self.assertEqual("dec", get_illion_prefix(10))
        self.assertEqual("septendec", get_illion_prefix(17))
        self.assertEqual("novemvigint", get_illion_prefix(29))
        self.assertEqual("unviginticent", get_illion_prefix(121))

    def test_numbers(self):
        self.assertEqual("1.23 million", format_illions(1_230_000))
        self.assertEqual("92.48 quadrillion", format_illions(92_482_138_592_145_241))


if __name__ == '__main__':
    unittest.main()
