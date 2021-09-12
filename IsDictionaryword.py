class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        freq={}
        for i in range(26):
            freq[B[i]]=i+1
        flag=1
        for i in range(len(A)-1):
            word=A[i]
            word2=A[i+1]
            flag=0
            for j in range(min(len(word),len(word2))):
                if freq[word[j]]>freq[word2[j]]:
                    return 0
                elif freq[word[j]]<freq[word2[j]]:
                    flag=1
                    break
                else:
                    flag=0
            if flag==0:
                if len(word)>len(word2):
                    return 0
                elif len(word)==len(word2):
                    return 1
            
        if flag==1:
            return 1     
          
if __name__ == '__main__':
    A=list(map(str,input().split(',')))
    B=str(input())
    s=Solution()
    n=s.solve(A,B)
    print(n)
