def solve(A,B):
    l=[]
    for i in B:
        l.append(list(A[i:]+A[0:i]))
    return l
        
            
def main():
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    n=len(A)
    for i in range(len(B)):
        B[i]=B[i]%n
    n=solve(A,B)
    for i in n:
        print(i)

if __name__ == '__main__':
    main()
