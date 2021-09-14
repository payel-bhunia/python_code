def solve(A):
    if len(A) in [0,1,2]:
        return 0
    else:
        A.sort()
        min_val=A[0]
        max_val=A[-1]
        if min_val!=max_val:
            start=1
            end=len(A)-2
            while(start<=end):
                if A[start]==min_val:
                    start+=1
                elif A[end]==max_val:
                    end-=1
                else:
                    return end-start+1
            return 0
        else:
            return 0
def main():
    A=list(map(int,input().split(',')))
    B=solve(A)
    print(B)

if __name__ == '__main__':
    main()
