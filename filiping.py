class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result=[]
        for i in image:
            i.reverse()
            result.append(i)
        k=0
        while k<len(result):
            j=0
            while(j<len(result)):
                if(result[k][j]==0):
                    result[k][j]=1
                else:
                    result[k][j]=0
                j+=1
            k+=1 
        return result     