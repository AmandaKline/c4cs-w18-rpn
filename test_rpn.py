import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)
	def test_adds(self):
		result = rpn.calculate('1 1 + 2 +')
		self.assertEqual(4, result)
	def test_subtract(self):
		result = rpn.calculate('5 2 -')
		self.assertEqual(3, result)
	def test_toomany(self):
		with self.assertRaises(TypeError):
			result = rpn.calculate('1 2 3 +')
	def test_mult(self):
		result = rpn.calculate('2 3 *')
		self.assertEqual(6, result)
	def test_div(self):
		result = rpn.calculate('4 2 /')
		self.assertEqual(2, result)
	def test_div_zero(self):
		result = rpn.calculate('2 2 + 4 0 / 2 +')
		self.assertEqual(6, result)
		result = rpn.calculate('0 0 - 4 0 . 2 +')
		self.assertEqual(2, result)
	def test_mod(self):
		result = rpn.calculate('5 4 %')
		self.assertEqual(1, result)
		result = rpn.calculate('4 5 %')
		self.assertEqual(4, result)
	def test_pow(self):
		result = rpn.calculate('2 3 ^')
		self.assertEqual(8, result)
	def test_int_div(self):
		result = rpn.calculate('2 3 .')
		self.assertEqual(0, result)
		result = rpn.calculate('3 2 .')
		self.assertEqual(1, result)
	def test_bit_and(self):
		result = rpn.calculate('1 1 &')
		self.assertEqual(1, result)
		result = rpn.calculate('2 1 &')
		self.assertEqual(0, result)
	def test_bit_or(self):
		result = rpn.calculate('1 1 |')
		self.assertEqual(1, result)
		result = rpn.calculate('2 0 |')
		self.assertEqual(2, result)
	def test_bit_not(self):
		result = rpn.calculate('1 ~')
		self.assertEqual(-2, result)
		result = rpn.calculate('4 ~')
		self.assertEqual(-5, result)




