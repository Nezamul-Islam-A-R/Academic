# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 20:13:31 2017

@author: Nezamul Islam A R
"""
import math
import random

x = [[1,1,0,0],[0,0,0,1],[1,0,0,0],[0,0,1,1]] #input
noOfNode = 2 #neuron [y1 Y2]
w = [[0.2,.8],[0.6,0.4],[0.5,0.7],[0.9,0.3]]
label = ['cluster 1','claster 2']
print('Init weight : ',w)
a = 0.6 #init learning rate
#iterate 100 times
def weightUpdate(a,x,w,indexPoint):
    for i in range(0,len(w)):
        w[i][indexPoint] = w[i][indexPoint] + a*(x[i] - w[i][indexPoint])

def dist(a,x,w,node):
    distFind = []
    for i in range(0,node):
        d = 0
        for j in range(0,len(x)):
            d += math.pow(x[j]-w[j][i],2)
        distFind.append(d)
    #print(distFind)
    minDist = min(distFind)
    indexPoint = distFind.index(minDist)
    weightUpdate(a,x,w,indexPoint)
    

for j in range(0,100):
    for i in range(0,len(x)):
        dist(a,x[i],w,noOfNode)
    a = a / 2

#testing
def testFindClass(x,node):
    distFind = []
    for i in range(0,node):
        d = 0
        for j in range(0,len(x)):
            d += math.pow(x[j]-w[j][i],2)
        distFind.append(d)
    #print(distFind)
    minDist = min(distFind)
    indexPoint = distFind.index(minDist)
    print('Class : ',label[indexPoint])

testInput = x #check    
testInput = [[1,1,1,1],[0,0,0,1],[1,1,1,0],[1,0,1,1]]
print('Updated weight : ',w)
for i in range(0,len(testInput)):
    testFindClass(testInput[i],noOfNode)
    
#r = random.random()
#r = random.uniform(0.001,.99)
#print(r)