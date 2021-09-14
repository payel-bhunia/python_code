def solve(A, B):
    #l=[]
    count=0
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i]+A[j]==B and i<j:
                return 1
    return 0
            
           
        
def main():
    A=list(map(int,input().split()))
    B=int(input())
    n=solve(A,B)
    print(n)

if __name__ == '__main__':
    main()
