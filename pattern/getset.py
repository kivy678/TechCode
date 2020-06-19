# -*- coding:utf-8 -*-

class TEST_EX:
	def __init__(self, test):
		self._test = test
 
	@property
	def test(self):
		return self._test

	@test.setter
	def test(self, test):
		self._test = test


a = TEST_EX('abc')
print(a.test)
a.test = 123
print(a.test)
