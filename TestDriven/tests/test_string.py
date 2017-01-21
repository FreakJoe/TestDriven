import unittest
from ..string import reverse

class TestString(unittest.TestCase):
	def test_reverse(self):
		self.assertEqual(reverse('hi'), 'ih')
		self.assertEqual(reverse('Hi'), 'iH')
		self.assertEqual(reverse('TestString'), 'gnirtStseT')