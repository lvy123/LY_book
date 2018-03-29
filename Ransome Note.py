"""Q:Ransom Note"""
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in set(ransomNote):
            if ransomNote.count(i)>magazine.count(i):
                return False
            
        return True
'''
describe the question:canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

相当于从magazine找出是否包含ransomNote字符串，如果有返回True，否则返回False


and something about use of set and count()
example:
str='name'
for i in set(str):
    print(i)
output
n
a
m
e

about count()
sentence='this is a python jupyter'
str='i'
sentence.count(str)

count(str,start=0,end=len(string))
"""

