# -*- codeing:utf-8 -*-

class A(object):
	def __init__(self):
		self.AC()

	def GetData(self):
		self.m_N = int(input())
		self.m_X = [int(x) for x in input().split()]

	def AC(self):
		self.GetData()
		ans = 0
		while self.m_X:
			self.m_Y = []
			for x in self.m_X:
				if x not in self.m_Y:
					self.m_Y.append(x)
			ans += (len(self.m_Y)-1)
			for x in self.m_Y:
				self.m_X.remove(x)
		print(ans)

A()

