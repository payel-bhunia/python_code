class Solution:
	# @param A : integer
	# @return an integer
	def colorful(self, A):
	    digits=[]
	    while(A>0):
	        digits.insert(0,A%10)
	        A=A//10
	    hash_set=set()
	    start=0
	    while(start<len(digits)):
	        end=start
	        while(end<len(digits)):
	            if start==end:
	                product=digits[start]
	            else:
	                product*=digits[end]
	            if product not in hash_set:
	                hash_set.add(product)
	            else:
	                return 0
	            end+=1
	        start+=1
	    return 1

       
          
if __name__ == '__main__':
    A=int(input())
    #B=int(input())
    s=Solution()
    n=s.colorful(A)
    print(n)
    exit()
