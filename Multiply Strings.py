class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a=['0','1','2','3','4','5','6','7','8','9']
        z=0
        x=0
        for i,element in enumerate(num1):
            for j in range(10):
                if num1[i]==a[j]:
                    z+=j*(10**i)
                    
        for a,b in enumerate(num2):
            for k in range(10):
                if num2[a]==a[k]:
                    x+=k*(10**a)
                    
        
        return(z*x)
