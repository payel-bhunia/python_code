class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def dNums(self, A, B):
	    hash_map={}
	    count=0
	    dist_cnt=[]
	    for i in range(B):
	        if A[i] in hash_map:
	            hash_map[A[i]]+=1
	        else:
	            hash_map[A[i]]=1
	            count+=1
	    dist_cnt.append(count)
	    for i in range(1,len(A)-B+1):
	        start=i
	        end=i+B-1
	        if hash_map[A[start-1]]>1:
	            hash_map[A[start-1]]-=1
	        else:
	            del hash_map[A[start-1]]
	            count-=1
	        if A[end] in hash_map:
	            hash_map[A[end]]+=1
	        else:
	            hash_map[A[end]]=1
	            count+=1
	        dist_cnt.append(count)
	    return dist_cnt
            
def main():
    A=list(map(int,input().split(',')))
    B=int(input())
    #print(C)
    s=Solution()
    n=s.dNums(A,B)
    print(n)

if __name__ == '__main__':
    main()
