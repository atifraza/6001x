# -*- coding: utf-8 -*-
#count = 0
#phrase = "hello, world"
#for iteration in range(5):
#    count += len(phrase)
#    print "Iteration " + str(iteration) + "; count is: " + str(count)

#x = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
#char = 'a'
#char in x
#
#cList = range(6, 1, -1)
#dList = []
#for num in cList:
#        dList.append(num)
#print(cList == dList)
#
#aList = range(1, 6)
#bList = aList
#aList[2] = 'hello'
#print(aList == bList)
#print(aList)
#print(bList)
#
#listA = [1, 4, 3, 0]
#listB = ['x', 'z', 't', 'q']
#print(listA.sort)
#print(listA.sort())
#print(listA)
#print('here')
#listA.insert(0, 100)
#listA.remove(3)
#listA.append(7)
#listA.extend([4, 1, 6, 3, 4])
#listA.pop(4)
#listA.reverse()
#print(listA)
#listB.sort()
#print(listB.pop())
#print(listB.count('a'))
#print(listA.extend([4,1,6,3,4]))
def swapSort(L): 
    """ L is a list on integers """
    print "Original L: ", L
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print L
    print "Final L: ", L

list1 = [0, 9, -20, 6, 8, 6, -100, 1, 0, 3, 2, 5]
swapSort(list1)