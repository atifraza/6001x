s = 'azcbobobegghakl'
bobCount = 0
for ind in range(len(s)):
    if s.count('bob', ind, ind+len('bob')) == 1:
        bobCount += 1
print('Number of times bob occurs is: ' + str(bobCount))