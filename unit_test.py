import unittest

from telnyx import Solution


from telnyx import Solution


class TestMethods(unittest.TestCase):
	def setUp(self):
		self.s=Solution()

	def test_palindrome(self):
		#Test list representation
		self.assertTrue(self.s.palindrome([0]))
		self.assertTrue(self.s.palindrome([1,2,1]))
		self.assertTrue(self.s.palindrome([1,67,1]))
		self.assertFalse(self.s.palindrome([1,2,3]))
		#Test string representation
		self.assertTrue(self.s.palindrome('0'))
		self.assertTrue(self.s.palindrome('1331'))
		self.assertFalse(self.s.palindrome('1321'))




	def test_convert(self):
		#Test base 10 convertion
		self.assertEqual(self.s.convert(11,10), '11')
		#Test other bases
		self.assertEqual(self.s.convert(19,2), [1,0,0,1,1])
		self.assertEqual(self.s.convert(33,2), [1,0,0,0,0,1])
		self.assertEqual(self.s.convert(995,16), [3,14,3])
		self.assertEqual(self.s.convert(997,996), [1,1])






if __name__ == '__main__':
    unittest.main()