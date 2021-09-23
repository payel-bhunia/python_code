def checkfreq(freqA,freqB):
    #print(freqA,freqB)
    for i in range(26):
        if freqA[i]!=freqB[i]:
            return False
    return True
def solve(A,B):
    freqA=[0]*26
    freqB=[0]*26
    lnA=len(A)
    lnB=len(B)
    count=0
    for i in A:
        index=ord(i)-ord('a')
        freqA[index]+=1
    #print(freqA)
    for i in range(lnA):
        index=ord(B[i])-ord('a')
        freqB[index]+=1
    #print(freqB)
    if checkfreq(freqA,freqB):
        count+=1
    #print(0,lnA-1)
    start=1
    end=start+lnA-1
    
    while(end<lnB):
        #print(start,end)
        index=ord(B[start-1])-ord('a')
        freqB[index]-=1
        index=ord(B[end])-ord('a')
        freqB[index]+=1
        start+=1
        end+=1
        if checkfreq(freqA,freqB):
            count+=1
    return count

def main():
    A=str(input())
    B=str(input())
    n=solve(A,B)
    print(n)

if __name__ == '__main__':
    main()
