def reverse(A,B):
    return A[len(A)-B:]+A[0:len(A)-B]
def main():
    l=input().split()
    A=[int(i) for i in l]
    B=int(input())
    B=B%A[0]
    n=reverse(A[1:],B)
    for i in n:
        print(i,end=" ")

if __name__ == '__main__':
    main()
