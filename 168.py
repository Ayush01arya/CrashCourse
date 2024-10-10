# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
#
# For example:
#
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...
# s="CDA"
# result=0
# for j in range (len(s)) :
#     result*=26
#     result+=ord(s[j])-ord('A')+1
#
#
# print(result)
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            index = (columnNumber - 1) % 26
            result = chr(index + ord('A')) + result
            columnNumber = (columnNumber - 1) // 26
        return result
