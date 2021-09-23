class Solution:
	# @param A : integer
	# @return an integer
	def reverse(self, A):
	    s=''
	    if A<0:
	        A=A*-1
	        s='-'
	    while(A>0):
	        s+=str(A%10)
	        A=A//10
	        if int(s)>0 and int(s)>(2**32)-1:
	            return 0
	        elif int(s)<0 and int(s)<-((2**31)-1):
	            return 0
	    return int(s)
def main():
    A=int(input())
    result=Solution()
    n=result.reverse(A)
    print(n)
    
if __name__ == '__main__':
    main()
