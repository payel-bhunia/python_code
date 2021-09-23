class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        pot=[0]*A
        for i in range(len(B)):
            s_ind=B[i][0]-1
            e_ind=B[i][1]-1
            pot[s_ind]+=B[i][2]
            if e_ind!=A-1:
                pot[e_ind+1]-=B[i][2]
        for i in range(1,A):
            pot[i]=pot[i-1]+pot[i]
        return pot
def main():
    A=int(input())
    B=int(input())
    C=[]
    for i in range(B):
        l=list(map(int,input().split()))
        C.append(l.copy())
        l.clear()
    #print(C)
    s=Solution()
    n=s.solve(A,C)
    print(n)

if __name__ == '__main__':
    main()
