"""
Author:Yijie Wu
Date: 11/20/2017
Dependency:sys
All rigths reserved
"""
class Solution(object):
	"""
	Given a positive int,return the 
	smallest base that makes it a palindrome num

	"""
	def get_smallestbase(self,num):
		for base in xrange(2,sys.maxint):
			if self.is_palindrome(num,base):
				return base

	"""
	Given a positive int,return the 
	True if this num of this base is
	palindrome, False, otherwise

	"""
	def is_palindrome(self,num,base):
		actual_num=self.convert(num,base)
		return self.palindrome(actual_num)


	"""
	Given a positive base 10 int,return the 
	list under that base if the base is not 10
	if base is 10 ,return the string representation
	"""
	def convert(self,num,base):
		if base==10:
			return str(num)
		res=[]
		while num != 0:
			remainder = num % base
			num= num/base   
			res.insert(0,remainder)
		return res


	"""
	Given a list/string,check if
	palindrome
	"""
	def palindrome(self,num):
		start=0
		end=len(num)-1
		while start<end:
			if num[start]!=num[end]:
				return False
			start+=1
			end-=1
		return True


import sys
def main():
	test1=Solution()
	with open ('result','w') as outfile:
		#User gives the ranges
		if len(sys.argv)==3:
			x=int(sys.argv[1])
			if x<=0:
				x=1
			y=int(sys.argv[2])
			if y<=0:
				y=1000

			if x>y:
				x=1
				y=1000
			for num in xrange(x,y+1):
				b=test1.get_smallestbase(num)
				print num,b
				outfile.write("%s,%s\n"%(num,b))

		#User did not give any range or wrong number of args
		else:
			for num in xrange(1,1001):
				b=test1.get_smallestbase(num)
				print num,b
				outfile.write("%s,%s\n"%(num,b))
	
if __name__ == '__main__':
	main()
