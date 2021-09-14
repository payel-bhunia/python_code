def solve(A):
    l=[]
    if len(A)<=2:
        return 0
    else:
        max_val=max(A[0],A[1])
        max_val2=min(A[0],A[1])
        for i in A[2:]:
            if i >max_val:
                max_val2=max_val
                max_val=i
            elif i>max_val2 and i<max_val:
                max_val2=i
                
        for i in A:
            if i<max_val2:
                l.append(i)
        return l
        
def main():
    A=list(map(int,input().split(',')))
    B=solve(A)
    print(B)

if __name__ == '__main__':
    main()
