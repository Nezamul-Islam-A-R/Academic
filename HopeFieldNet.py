# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 10:12:11 2017

@author: Nezamul Islam A R
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 08:54:27 2017

@author: Nezamul Islam A R
"""




noOfneuron =8
synapsisLink = (noOfneuron**2) - noOfneuron

x1 = [1,-1,1,-1,1,-1,1,-1]               
x2 = [1,1,1,1,-1,-1,-1,-1]
testSet = [-1,1,1,1,-1,-1,-1,-1] 
testSet1 = testSet 

testcal = [0 for i in range(noOfneuron)]
inx1 = [0 for i in range(noOfneuron)]
inx2 = [0 for i in range(noOfneuron)]
weightMat = [[0 for i in range(noOfneuron)] for y in range(noOfneuron)]
#Update weight

def updateWeight(x1,x2,noOfneuron):
    mat1x = [[0 for i in range(noOfneuron)] for y in range(noOfneuron)]
    mat2x = [[0 for i in range(noOfneuron)] for y in range(noOfneuron)]
    
    for i in range(0,noOfneuron):
        for j in range(0,noOfneuron):
            if(i  != j):
                mat1x[i][j] = x1[i]*x1[j]
                mat2x[i][j] = x2[i]*x2[j]
    
#    print(mat1x)
#    print(mat2x)            
    weightMat = [[mat1x[i][j] + mat2x[i][j]  for j in range(len(mat1x[0]))] for i in range(len(mat1x))]
    return weightMat


wM = updateWeight(x1,x2,noOfneuron)
for i in range(0,noOfneuron):
    print(wM[i])

tTimes = [[0 for i in range(noOfneuron)] for y in range(2)]


def activeDynamic(wM,testSet1,testcal,noOfneuron):
    flag = 1
    tTimes[0] = testSet1
    for i in range(0,noOfneuron):
        xR = 0
        for j in range(0,noOfneuron):
            a = testSet1[j]*wM[i][j]
            xR += a
#            print(a,end =' ')
#        print('= ',xR)
            
        if(xR >= 0):
            xR = 1
        else:
            xR = -1
        testcal[i] = xR
    tTimes[1] = testcal
               
    for i in range(0,len(testSet)):
        if(tTimes[0][i] != tTimes[1][i]):
            flag = 0
            break
#    print(tTimes)
    return testcal,flag
    
              
flag = 0
iteration = 0
while(flag != 1): 
    iteration += 1           
    testcal,flag = activeDynamic(wM,testSet1,testcal,noOfneuron)
    testSet1 = testcal
    if(flag == 1):
        print('Output: ',testcal)
    testcal = [0 for i in range(noOfneuron)]

    
print('Stable after iter : ',iteration)  
    
               
               
