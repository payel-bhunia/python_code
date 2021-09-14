def solve(A):
    max_even=-1e9
    min_odd=1e9
    for i in A:
        if i%2==0:
            max_even=max(max_even,i)
        else:
            min_odd=min(min_odd,i)
    return max_even-min_odd
        
def main():
    A=list(map(int,input().split(',')))
    B=solve(A)
    print(B)

if __name__ == '__main__':
    main()
