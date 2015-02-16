#count = 0
#phrase = "hello, world"
#for iteration in range(5):
#    count += len(phrase)
#    print "Iteration " + str(iteration) + "; count is: " + str(count)

x = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
char = 'a'
char in x

cList = range(6, 1, -1)
dList = []
for num in cList:
        dList.append(num)
print(cList == dList)

aList = range(1, 6)
bList = aList
aList[2] = 'hello'
print(aList == bList)
print(aList)
print(bList)

listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']
print(listA.sort)
print(listA.sort())
print(listA)
print('here')
listA.insert(0, 100)
listA.remove(3)
listA.append(7)
listA.extend([4, 1, 6, 3, 4])
listA.pop(4)
listA.reverse()
print(listA)
listB.sort()
print(listB.pop())
print(listB.count('a'))
print(listA.extend([4,1,6,3,4]))
