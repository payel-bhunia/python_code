class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        min_diff=abs(A[0]-A[1])
        print(min_diff)
        for i in range(1,len(A)-1):
            print(abs(A[i]-A[i+1]))
            min_diff=min(min_diff,abs(A[i]-A[i+1]))
        print(min_diff)
        return min_diff
        

            
def main():
    A=list(map(int,input().split(',')))
    B=int(input())
    #print(C)
    s=Solution()
    n=s.solve(A)
    print(n)

if __name__ == '__main__':
    main()
