s = 'azcbobobegghakl'
strList = []
tempStr = s[0]

for ind in range(1,len(s)):
    if (tempStr[-1]<=s[ind]):
        tempStr = tempStr + s[ind]
    else:
        strList.append(tempStr)
        tempStr = s[ind]

strList.append(tempStr)        
maxLenList = 0
maxLen = 0
for ind in range(len(strList)):
    currLen = len(strList[ind])
    if (maxLen < currLen):
        maxLen = currLen
        maxLenList = ind

print('Longest substring in alphabetical order is: ' + strList[maxLenList])