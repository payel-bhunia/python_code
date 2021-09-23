class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n=len(A)
        sum=0
        min_sum=0
        hash_map=[0]*(n-B+1)
        for i in range(n):
            sum+=A[i]
        min_sum=sum
        hash_map[0]=min_sum
        for i in range(1,n-B+1):
            start=i
            end=i+B-1
            sum=sum-A[start-1]+A[end]
            hash_map[i]=sum
            min_sum=min(min_sum,sum)
        for i in range(n-B+1):
            if hash_map[i]==min_sum:
                return i
        

            
def main():
    A=list(map(int,input().split(',')))
    B=int(input())
    #print(C)
    s=Solution()
    n=s.solve(A,B)
    print(n)

if __name__ == '__main__':
    main()
