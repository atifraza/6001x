# -*- coding: utf-8 -*-
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
        
def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    curr = atMe
    if (newFrob.myName() > curr.myName()):
        if curr.getAfter():
            while newFrob.myName() > curr.getAfter().myName():
                if curr.getAfter():
                    curr = curr.getAfter()
                else:
                    break
        newFrob.setAfter(curr.getAfter())
        newFrob.setBefore(curr)
        curr.setAfter(newFrob)
        if newFrob.getAfter():
            newFrob.getAfter().setBefore(newFrob)
    elif (newFrob.myName() <= curr.myName()):
        if curr.getBefore():
            while newFrob.myName() <= curr.getBefore().myName():
                if curr.getBefore():
                    curr = curr.getBefore()
                else:
                    break
        newFrob.setBefore(curr.getBefore())
        newFrob.setAfter(curr)
        curr.setBefore(newFrob)
        if newFrob.getBefore():
            newFrob.getBefore().setAfter(newFrob)

def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    # Your Code Here
    if start.getBefore():
        return findFront(start.getBefore())
    else:
        return start
    

#
#test_list = Frob('mark')
#c = Frob('craig')
#
#insert(test_list, Frob("sam"))
#insert(test_list, Frob("nick"))
#insert(test_list, c)
#insert(c, Frob("xanthi"))

eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)
findFront(fred)