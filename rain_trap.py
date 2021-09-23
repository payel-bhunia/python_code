class Solution:
	# @param A : tuple of integers
	# @return an integer
	def trap(self, A):
	    n=len(A)
	    if n<=2:
	        return 0
	    else:
	        R_max=[0]*n
	        L_max=[]
	        L_max.append(A[0])
	        for i in range(1,n):
	            L_max.append(max(L_max[i-1],A[i]))
	        
	        R_max[n-1]=A[n-1]
	        last_val=A[n-1]
	        i=n-2
	        while(i>=0):
	            last_val=max(last_val,A[i])
	            R_max[i]=last_val
	            i-=1
	        trap_sum=0
	        for i in range(1,n-1):
	            if min(L_max[i],R_max[i])>A[i]:
	                trap_sum+=min(L_max[i],R_max[i])-A[i]
	        return trap_sum
def main():
    A=list(map(int,input().split(' ')))
    B=Solution()
    n=B.trap(A)
    print(n)

if __name__ == '__main__':
    main()
