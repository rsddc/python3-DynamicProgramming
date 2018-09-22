# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 00:48:29 2018

@author: rakesh sharma
"""

instr='abc'
inList=['a','b','c']
def printsubstrings(instr,outstr):
    if len(instr)==0:
        print(outstr)
        return

        
    else:
        printsubstrings(instr[1:],outstr)
        printsubstrings(instr[1:],outstr+instr[0])
print("Printing all substrings of a give string:-",instr)        
printsubstrings(instr,'')  #USING STRING
print("==============================================")

def sublists(inlist,outlist):
    
    if len(inlist) == 0:
        print(outlist)
        return
    else:
        sublists(inlist[1:],outlist)
        sublists(inlist[1:],outlist+[inlist[0]])
    
print("Printing all sub Lists of a give List:-",inList)     
sublists(inList,[])  #USEING LIST
print("==============================================")
#Returing list
l=[]
def subsequLists(inList,outList):
    
    if len(inList) == 0:
        #print(outList,end=' ')
        l.append([outList])
        return
    else:
        subsequLists(inList[1:],outList)
        subsequLists(inList[1:],outList+inList[0])
        
print("Return all sub Lists of a give List:-")  
subsequLists(['a'],'')    
print(l,len(l))    
print("==============================================")