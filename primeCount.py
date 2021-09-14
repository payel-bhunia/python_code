def solve(A):
    count=0
    for i in range(len(A)):
        if A[i]&1==1 and A[i]>1 and A[i]!=2:
            j=3
            isPrime=True
            while(j*j<=A[i]):
                if A[i]%j==0:
                    isPrime=False
                    break
                else:
                    j+=1
            if isPrime==True:
                #print(A[i])
                count+=1
        elif A[i] in [2,3,5,7]:
            count+=1
    return count
        
            
def main():
    A=list(map(int,input().split()))
    n=solve(A)
    print(n)

if __name__ == '__main__':
    main()
