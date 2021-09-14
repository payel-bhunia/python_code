def solve(A):
    l=[]
    l_sub=[]
    for i in range(A):
        l_sub=[]
        for j in range(A):
            if j<=i:
                l_sub.append(j+1)
            else:
                l_sub.append(0)
        l.append(l_sub)
    return l        
        
def main():
    A=int(input())
    B=solve(A)
    print(B)

if __name__ == '__main__':
    main()
