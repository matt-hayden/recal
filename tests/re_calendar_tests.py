from datetime import datetime
import unittest

import recal

class ReCalendarCase(unittest.TestCase):
	def test_get_similar_months_default(self):
		for y, m in recal.get_similar_months():
			self.assertTrue( (y,m) == (2019,1) )
			break
	def test_get_similar_months(self):
		for y, m in recal.get_similar_months(2016, 12):
			self.assertTrue( (y,m) == (2005,12) )
			break


if __name__ == '__main__':
	unittest.main()
