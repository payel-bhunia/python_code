def solve(A):
    l=[]
    prev=A[0]
    l.append(prev)
    for i in range(1,len(A)):
        if (prev+A[i])%2!=0:
            l.append(A[i])
            prev=A[i]
    return l
        
            
def main():
    A=list(map(int,input().split()))
    if len(A)==0:
        return 0
    elif len(A)==1:
        return 1
    else:
    #B=int(input())
        n=solve(A)
        print(n)

if __name__ == '__main__':
    main()
