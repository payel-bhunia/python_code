class Solution:
	# @param A : string
	# @return an integer
	def titleToNumber(self, A):
	    alpha={}
	    for i in range(26):
	        alpha[chr(ord('A')+i)]=i+1
	    n=len(A)
	    i=0
	    val=0
	    while(i<n):
	        val+=alpha[A[n-i-1]]*(26**i)
	        i+=1
	    return val
def main():
    A=str(input())
    result=Solution()
    n=result.titleToNumber(A)
    print(n)
    
if __name__ == '__main__':
    main()
