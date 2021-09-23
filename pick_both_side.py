class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n=len(A)
        pref_odd=[0]*n
        pref_even=[0]*n
        pref_even[0]=A[0]
        pref_odd[0]=0
        count=0
        for i in range(1,n):
            if i%2==0:
                pref_even[i]=pref_even[i-1]+A[i]
                pref_odd[i]=pref_odd[i-1]
            else:
                pref_even[i]=pref_even[i-1]
                pref_odd[i]=pref_odd[i-1]+A[i]
        even_b=0
        even_a=0
        odd_b=0
        odd_a=0
        for i in range(n):
            if i==0:
                even_b=0
                odd_b=0
            else:
                even_b=pref_even[i-1]
                odd_b=pref_odd[i-1]
            even_a=pref_even[n-1]-pref_even[i]
            odd_a=pref_odd[n-1]-pref_odd[i]
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
