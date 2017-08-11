import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

x = [[1,0,0],[4,1,1],[1,1,0],[5,1,1],[2,3,0],[3,0,1],[1,2,0],[4,0,1],[5,0,1]]
w = [1,1]
w0 = 0 #as bias #Threshold = 5 suppose
x0 = 1 # as Fixed
colors = 40*['g.',"r.","c.","b.","k.","y.",'m.'] 
delt  = 100
n = .025 #eeta
flag = 0
dt = 0
ij = 1
count = 1
while(flag != 1):
    count = 0
    for i in range(0,len(x)):
        summ = w0*x0
        y = x[i][2]       
        for j in range(0,2):
            summ += w[j]*x[i][j]
        if(summ > 0):
            dt = 1
        else:
            dt = 0        
        delt = dt - y
        #print(w[0],' ',w[1])
        if(delt == 0):            
            count+=1
        if(delt != 0):
            for l in range(0,2):
                w0 = w0 - n*delt*x[i][l]
                w[l] = w[l] - n*delt*x[i][l]
    if(count == len(x)):
        flag = 1    
    
#print(w0,' ',w)

label = ['Class 0','Class 1']  
labels = [0,1]     
testInput = x
def showClass(x0,w0,w,test):
    #print(x0,' ',w0,' ',w,' ',test)
    for j in range(0,len(test)):
        summ = w0*x0
        for i in range(0,2):
            summ += test[j][i]*w[i]
        if(summ >0):
            dt = 1
        else:
            dt = 0
        print(test[j],' ',label[dt])
showClass(x0,w0,w,testInput)     


for i in range(0,len(x)):
    plt.plot(x[i][0],x[i][1],colors[labels[x[i][2]]],markersize = 50)
plt.show()

      