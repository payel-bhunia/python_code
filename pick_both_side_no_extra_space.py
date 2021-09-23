class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n=len(A)
        count=0
        even_sum=0
        odd_sum=0
        for i in range(n):
            if i%2==0:
                even_sum+=A[i]
            else:
                odd_sum+=A[i]
        #print(even_sum,odd_sum)
        even_b=0
        even_a=0
        odd_b=0
        odd_a=0
        for i in range(n):
            if i%2==0:
                if i==0:
                    even_b=0
                    odd_b=0
                else:
                    odd_b+=A[i-1]
                even_a=even_sum-A[i]-even_b
                odd_a=odd_sum-odd_b
            else:
                if i==1:
                    odd_b=0
                even_b+=A[i-1]    
                even_a=even_sum-even_b
                odd_a=odd_sum-odd_b-A[i]
            if even_b+odd_a==odd_b+even_a:
                count+=1
        return count

def main():
    A=list(map(int,input().split(',')))
    #B=int(input())
    #print(C)
    s=Solution()
    n=s.solve(A)
    print(n)

if __name__ == '__main__':
    main()
