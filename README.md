**Genetic Algorithm (GA) [Acdemic Codes]**

**Knapsack**

**1. Inputs:**

```
weight =  [ 763783, 914370, 831207, 100284, 487486, 182921, 369532, 727094, 272162, 227474, 170387, 697344 ,266796, 41169 ,937876, 883615 ,923090 ,385246 ,839734 ,423575, 33377, 975193, 69579, 418849];
profit =  [1559844, 1724668, 1548321, 186455, 1012952, 337633, 806295, 1329837, 546869, 446874, 316848, 1399126, 578882, 79486, 1816706, 1665934, 1917601, 770200, 1732704, 806240, 65751, 1870594, 140713, 859568];
cap = 5971071; 
```

**1. Outputs:**

```
Itemize W-P :  0  >  [763783, 1559844]
Itemize W-P :  1  >  [914370, 1724668]
Itemize W-P :  2  >  [831207, 1548321]
Itemize W-P :  3  >  [100284, 186455]
Itemize W-P :  4  >  [487486, 1012952]
Itemize W-P :  5  >  [182921, 337633]
Itemize W-P :  6  >  [369532, 806295]
Itemize W-P :  7  >  [727094, 1329837]
Itemize W-P :  8  >  [272162, 546869]
Itemize W-P :  9  >  [227474, 446874]
Itemize W-P :  10  >  [170387, 316848]
Itemize W-P :  11  >  [697344, 1399126]
Itemize W-P :  12  >  [266796, 578882]
Itemize W-P :  13  >  [41169, 79486]
Itemize W-P :  14  >  [937876, 1816706]
Itemize W-P :  15  >  [883615, 1665934]
Itemize W-P :  16  >  [923090, 1917601]
Itemize W-P :  17  >  [385246, 770200]
Itemize W-P :  18  >  [839734, 1732704]
Itemize W-P :  19  >  [423575, 806240]
Itemize W-P :  20  >  [33377, 65751]
Itemize W-P :  21  >  [975193, 1870594]
Itemize W-P :  22  >  [69579, 140713]
Itemize W-P :  23  >  [418849, 859568]
Population :  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] fitness :  [1037594, 2043142]
Population :  [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0] fitness :  [2157206, 4337968]
Population :  [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] fitness :  [1789975, 3531032]
Population :  [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] fitness :  [1211423, 2312255]
Population :  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] fitness :  [1299616, 2494868]
Population :  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0] fitness :  [2558310, 5133433]
Population :  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] fitness :  [1528551, 2947447]
Population :  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0] fitness :  [1890637, 3860044]
Epoch >  1   Final result :  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]  Fitness :  [3322093, 6693277]
Epoch >  2   Final result :  [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]  Fitness :  [3877003, 7694706]
Epoch >  3   Final result :  [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]  Fitness :  [3977287, 7881161]
Epoch >  4   Final result :  [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]  Fitness :  [4891657, 9605829]
Epoch >  5   Final result :  [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]  Fitness :  [4891657, 9605829]
Epoch >  6   Final result :  [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]  Fitness :  [4891657, 9605829]
Epoch >  7   Final result :  [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]  Fitness :  [4891657, 9605829]
Epoch >  8   Final result :  [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]  Fitness :  [5167954, 10152721]
Epoch >  9   Final result :  [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]  Fitness :  [5838361, 11503306]
Epoch >  10   Final result :  [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]  Fitness :  [5838361, 11503306]
Epoch >  11   Final result :  [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]  Fitness :  [5838361, 11503306]
Epoch >  12   Final result :  [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]  Fitness :  [5838361, 11503306]
Epoch >  13   Final result :  [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]  Fitness :  [5838361, 11503306]
Epoch >  14   Final result :  [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]  Fitness :  [5838361, 11503306]
Epoch >  15   Final result :  [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]  Fitness :  [5838361, 11503306]
Epoch >  16   Final result :  [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]  Fitness :  [5838361, 11503306]
Epoch >  17   Final result :  [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]  Fitness :  [5838361, 11503306]
Epoch >  18   Final result :  [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]  Fitness :  [5838361, 11503306]
Epoch >  19   Final result :  [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]  Fitness :  [5838361, 11503306]
Epoch >  20   Final result :  [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]  Fitness :  [5838361, 11503306]

GA Result:
Final result :  [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]  Fitness :  [5838361, 11503306]
Used Time 0.08431029319763184 s
```

**2. Inputs:**

```
itemize = [[7,3],[3,5],[8,4],[3,9],[9,10],[11,6]] #_W_&_P_
maxW = 20
```

**2. Outputs:**

```
Itemize W-P :  0  >  [7, 3]
Itemize W-P :  1  >  [3, 5]
Itemize W-P :  2  >  [8, 4]
Itemize W-P :  3  >  [3, 9]
Itemize W-P :  4  >  [9, 10]
Itemize W-P :  5  >  [11, 6]
Population :  [0, 1, 1, 0, 1, 1] fitness :  [31, 25]
Population :  [1, 1, 0, 1, 0, 1] fitness :  [24, 23]
Population :  [0, 1, 0, 0, 0, 0] fitness :  [3, 5]
Population :  [1, 0, 0, 0, 1, 0] fitness :  [16, 13]
Population :  [0, 1, 1, 1, 0, 1] fitness :  [25, 24]
Population :  [0, 1, 0, 0, 1, 1] fitness :  [23, 21]
Population :  [0, 1, 0, 0, 0, 0] fitness :  [3, 5]
Population :  [1, 1, 1, 0, 0, 1] fitness :  [29, 18]
Epoch >  1   Final result :  [1, 1, 0, 1, 0, 0]  Fitness :  [13, 17]
Epoch >  2   Final result :  [1, 1, 0, 1, 0, 0]  Fitness :  [13, 17]
Epoch >  3   Final result :  [1, 1, 0, 0, 1, 0]  Fitness :  [19, 18]
Epoch >  4   Final result :  [0, 1, 0, 1, 0, 1]  Fitness :  [17, 20]
Epoch >  5   Final result :  [0, 1, 0, 1, 1, 0]  Fitness :  [15, 24]
Epoch >  6   Final result :  [0, 1, 0, 1, 1, 0]  Fitness :  [15, 24]
Epoch >  7   Final result :  [0, 1, 0, 1, 1, 0]  Fitness :  [15, 24]
Epoch >  8   Final result :  [0, 1, 0, 1, 1, 0]  Fitness :  [15, 24]

GA Result:
Final result :  [0, 1, 0, 1, 1, 0]  Fitness :  [15, 24]
Actual output :  [15, 24]
Used Time 0.022340774536132812 s
```

**Travelling Sales Man (TSP)**

**Inputs**

```
#Cities are [1,2,3,4,5]
#Cost matrix = 5*5 matrix
[[0,10,8,9,7],[10,0,10,5,6],[8,10,0,8,9],[9,5,8,0,6],[7,6,9,6,0]]
```

**Outputs**

```
Cost City:  1  >  [0, 10, 8, 9, 7]
Cost City:  2  >  [10, 0, 10, 5, 6]
Cost City:  3  >  [8, 10, 0, 8, 9]
Cost City:  4  >  [9, 5, 8, 0, 6]
Cost City:  5  >  [7, 6, 9, 6, 0]
Population > 0  :  [1, 5, 3, 4, 2, 1] fitness :  39
Population > 1  :  [1, 5, 2, 3, 4, 1] fitness :  40
Population > 2  :  [1, 2, 5, 3, 4, 1] fitness :  42
Population > 3  :  [1, 5, 3, 2, 4, 1] fitness :  40
Population > 4  :  [1, 5, 3, 2, 4, 1] fitness :  40
Population > 5  :  [1, 4, 5, 2, 3, 1] fitness :  39
Population > 6  :  [1, 5, 4, 2, 3, 1] fitness :  36
Population > 7  :  [1, 3, 4, 2, 5, 1] fitness :  34
Epoch >  1   Final result :  [1, 5, 4, 2, 3, 1]  Fitness :  36
Epoch >  2   Final result :  [1, 5, 2, 4, 3, 1]  Fitness :  34
Epoch >  3   Final result :  [1, 5, 4, 2, 3, 1]  Fitness :  36
Epoch >  4   Final result :  [1, 5, 2, 4, 3, 1]  Fitness :  34
Epoch >  5   Final result :  [1, 5, 2, 4, 3, 1]  Fitness :  34
Epoch >  6   Final result :  [1, 5, 2, 4, 3, 1]  Fitness :  34
Epoch >  7   Final result :  [1, 5, 2, 4, 3, 1]  Fitness :  34
Epoch >  8   Final result :  [1, 5, 2, 4, 3, 1]  Fitness :  34
Epoch >  9   Final result :  [1, 5, 2, 4, 3, 1]  Fitness :  34

GA Result:
Final result :  [1, 5, 2, 4, 3, 1]  Fitness :  34
Actual output :  [1, 3, 4, 2, 5, 1]  Cost :  34
Used Time 0.016005754470825195 s
```


**Self Organizing Map (SOM)**

**Inputs**

```
x = [[1,1,0,0],[0,0,0,1],[1,0,0,0],[0,0,1,1]] #input
noOfNode = 2 #neuron [y1 Y2]
w = [[0.2,.8],[0.6,0.4],[0.5,0.7],[0.9,0.3]]
```

**Outputs**

```
Init weight :  [[0.2, 0.8], [0.6, 0.4], [0.5, 0.7], [0.9, 0.3]]
Updated weight :  [[0.00832704630559306, 0.9916729536944068], [0.024981138916779177, 0.4135348745694803], [0.5823016022777234, 0.02914466206957569], [0.9958364768472036, 0.012490569458389588]]
Class :  cluster 1
Class :  cluster 1
Class :  claster 2
Class :  cluster 1

**Perceptron**

**Inputs**

```
x = [[1,0,0],[4,1,1],[1,1,0],[5,1,1],[2,3,0],[3,0,1],[1,2,0],[4,0,1],[5,0,1]]
w = [1,1]
```

**Outputs**

```
[1, 0, 0]   Class 0
[4, 1, 1]   Class 1
[1, 1, 0]   Class 0
[5, 1, 1]   Class 1
[2, 3, 0]   Class 0
[3, 0, 1]   Class 1
[1, 2, 0]   Class 0
[4, 0, 1]   Class 1
[5, 0, 1]   Class 1
```

![image](https://user-images.githubusercontent.com/20375942/171592803-ec77b8ed-b6c3-4b2a-b311-0513ac7322fc.png)

**Hope field network**

**Inputs**

```
x1 = [1,-1,1,-1,1,-1,1,-1]               
x2 = [1,1,1,1,-1,-1,-1,-1]
testSet = [-1,1,1,1,-1,-1,-1,-1] 
```

**Outputs**

```
[0, 0, 2, 0, 0, -2, 0, -2]
[0, 0, 0, 2, -2, 0, -2, 0]
[2, 0, 0, 0, 0, -2, 0, -2]
[0, 2, 0, 0, -2, 0, -2, 0]
[0, -2, 0, -2, 0, 0, 2, 0]
[-2, 0, -2, 0, 0, 0, 0, 2]
[0, -2, 0, -2, 2, 0, 0, 0]
[-2, 0, -2, 0, 0, 2, 0, 0]
Output:  [1, 1, 1, 1, -1, -1, -1, -1]
Stable after iter :  2
```
