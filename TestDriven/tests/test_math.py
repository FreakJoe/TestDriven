import unittest
from ..math import square

class TestMath(unittest.TestCase):
	def test_square(self):
		self.assertEqual(square(2), 4)
		self.assertEqual(square(4), 16)
		self.assertEqual(square(6), 36)