def plusOne(A):
    i=len(A)-1
    carry=0
    while(i>=0):
        if A[i]<9:
            if i==len(A)-1:
                A[i]+=1
            elif carry==1:
                A[i]+=carry
            carry=0
            break
        else:
            A[i]=0
            carry=1
            i-=1
    if carry==1:
        A.insert(0,1)
    start=0
    while(start<len(A)):
        if A[start]!=0:
            break
        else:
            start+=1
                
    return A[start:]

def main():
    A=list(map(int,input().split()))
    n=plusOne(A)
    print(n)

if __name__ == '__main__':
    main()
