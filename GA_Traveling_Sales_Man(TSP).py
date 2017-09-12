# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 12:15:24 2017

@author: Nezamul Islam A R
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 13:13:23 2017

@author: Nezamul Islam A R
"""
import random
import time
start_time = time.time()

#Cities are [1,2,3,4,5]
#Cost matrix = 5*5 matrix

cost_Matrix_Function = [[0,10,8,9,7],[10,0,10,5,6],[8,10,0,8,9],[9,5,8,0,6],[7,6,9,6,0]] #Cities_&_Cost #itemize
no_of_Cities = len(cost_Matrix_Function) #5 #no_of_population 

visited_root = no_of_Cities + 1 #6 #population_No
population_No = 8

c,r = visited_root,population_No;
population = [[0 for x in range(c)] for y in range(r)] 

fitness_col = 1
fitness = [0 for y in range(r)] #cost for every population #_r = 8 #Example: [39,32,90,99,80]

def callRandPos(c):
    mat1 = random.sample(range(2,6), c)#city #pos 0,5 fixed
    #print('rand City : ',mat1)
    return (mat1)    
def calcFitness(cross_Result_Population,no_of_Cities):
    fitness = [0 for y in range(r)]
    for i in range(0,len(cross_Result_Population)):
        cost = 0
        for j in range(0,no_of_Cities):
            row = cross_Result_Population[i][j] - 1
            col = cross_Result_Population[i][j+1] - 1
            cost += cost_Matrix_Function[row][col]
            #print('cost >> ',i,' : ',cost)
        fitness[i] = cost

    return(fitness)
    
def initPopulation(population,fitness,r,generate_c,no_of_Cities):    
    
    for i in range(0,r): #r = 8         
        ran2 = callRandPos(generate_c)  
        population[i][0] = 1 #pos  = 0
        population[i][visited_root-1] = 1 #pos = 5    
              
        for j in range(1,generate_c+1):
            population[i][j] = ran2[j-1]                      
    fitness = calcFitness(population,no_of_Cities) 
           
    return(population,fitness)
            
generate_c = 4 #rand 4 cities
population,fitness = initPopulation(population,fitness,r,generate_c,no_of_Cities)

for i in range(0,no_of_Cities):
    print('Cost City: ',i+1,' > ',cost_Matrix_Function[i])
    
for i in range(0,population_No):
    print('Population >',i,' : ',population[i],'fitness : ',fitness[i])
   
def final_result(population,fitness):
    loc = 0
    minm = 1200
    for i in range(0,len(population)):
        if(fitness[i] < minm):
           minm = fitness[i]
           loc = i
    print('Final result : ',population[loc],' Fitness : ',fitness[loc])

def tournament_Selection_Call(randSelection,fitness,selection_no): #[[6, 4, 1], [3, 4, 0], [5, 7, 2], [1, 3, 5]]
    best_Cross = [[0 for x in range(2)] for y in range(len(randSelection))] #r = 4, c = 2
    minP = 0
    dis = []
    store_i = 0
    for j in range(0,len(randSelection)):        
        posDiscard = 0
        for i in range(0,selection_no):
            if(fitness[randSelection[j][i]] > minP):
                minP = fitness[randSelection[j][i]]
                store_i = i
                
        posDiscard = randSelection[j][store_i]
        dis.append(posDiscard)
                
    for i in range(0,len(randSelection)):
        x = 0
        for j in range(0,selection_no):
            if(dis[i] != randSelection[i][j]):
                best_Cross[i][x] = randSelection[i][j]
                x += 1      
    #print('Discard : ',dis)
    #print('rand Cross : ',randSelection,' best Cross :',best_Cross)
    return(best_Cross)
        
def crossOver_Call(best_Cross,population,population_No,visited_root,fitness_col,r): 
    #best = [[3, 1], [6, 1], [1, 0], [3, 0]]     
    no_Cross = len(best_Cross) * 2
    cross_Result = [[0 for x in range(visited_root)] for y in range(no_Cross)] #8
    #cross_Fitness_Result  
    Q = 0
    for j in range(0,len(best_Cross)):
        rand = int(random.uniform(1,visited_root-2)) #random point choose (1-4)
        #print('rand : ',rand)
        for i in range(0,visited_root):
            if(i <= rand):
                cross_Result[Q][i] = population[best_Cross[j][0]][i]
                cross_Result[Q+1][i] = population[best_Cross[j][1]][i]
            else:
                cross_Result[Q][i] = population[best_Cross[j][0]][i]
                cross_Result[Q+1][i] = population[best_Cross[j][1]][i]
        Q += 2
    #fitness_Cross = calcFitness(cross_Result,visited_root)
    #print('fitness Cross : ',fitness_Cross)    
    return(cross_Result)    

def mutaion(cross_Result):
    for i in range(0,len(cross_Result)):
        ran_Mutation_Point = random.sample(range(1,no_of_Cities-1), 2)     
        
        temp = cross_Result[i][ran_Mutation_Point[0]]
        cross_Result[i][ran_Mutation_Point[0]] = cross_Result[i][ran_Mutation_Point[1]]
        cross_Result[i][ran_Mutation_Point[1]] = temp
        
    mut_Fitness = calcFitness(cross_Result,no_of_Cities)
    
    return(cross_Result,mut_Fitness)
            
def newPopulation(mutationPopulation,mutaionFitness,population,fitness,no_of_Cities):
    fitness_Old = calcFitness(population,no_of_Cities)
    fitness_New = calcFitness(mutationPopulation,no_of_Cities)
    max1,max2 = 1000,1000
    for i in range(0,len(fitness_Old)):
        if(fitness_Old[i] < max1):
            max1 = fitness_Old[i]
        elif(fitness_Old[i] < max2):
            max2 = fitness_Old[i]
    pos1Old = fitness_Old.index(max1)
    pos2Old = fitness_Old.index(max2)
    
    max1,max2 = 0,0
    for i in range(0,len(fitness_New)):
        if(fitness_New[i] > max1):
            max1 = fitness_New[i]
        elif(fitness_New[i] > max2):
            max2 = fitness_New[i]
            
    pos1New = fitness_New.index(max1)
    pos2New = fitness_New.index(max2)

    for i in range(0,len(population)):
        if(i == pos1New):
            for j in range(0,no_of_Cities):
                mutationPopulation[i][j] = population[pos1Old][j]
        elif(i == pos2New):
            for j in range(0,no_of_Cities):
                mutationPopulation[i][j] = population[pos2Old][j]
        else:
            for j in range(0,no_of_Cities):
                mutationPopulation[i][j] = population[i][j]
        population = mutationPopulation        
    return(population)

    
def selection_N_crossover_N_mutation(population,fitness,population_No,no_of_Cities,visited_root):
    selection_no = 3
    findCrossPoint = int(population_No / 2)
    randSelection = [[0 for x in range(selection_no)] for y in range(findCrossPoint)]
    for j in range(0,findCrossPoint):
        randSelection[j] = random.sample(range(0,population_No), 3) #mat_4*3 #[[2, 4, 7], [0, 2, 7], [6, 3, 7], [7, 2, 6]] random 3 select
    #print(randSelection)
    best_Cross = tournament_Selection_Call(randSelection,fitness,selection_no) #[3,2] best two for cross over
    #print('Best_Cross : ',best_Cross)    
    cross_Result = crossOver_Call(best_Cross,population,population_No,visited_root,fitness_col,r)
    cross_Fitness_Result = calcFitness(cross_Result,no_of_Cities)
    #print('Cross Over : ',cross_Result,'  :  ',cross_Fitness_Result) 
    mutationPopulation,mutaionFitness = mutaion(cross_Result)
    #print('Mutation : ',mutationPopulation,'  :  Mutation Fitness : ',mutaionFitness)
    new_population = newPopulation(mutationPopulation,mutaionFitness,population,fitness,no_of_Cities)
    #new_population = population
    return(new_population)


def GA_knapsack(population,fitness,population_No,no_of_Cities,visited_root):
    new_population = selection_N_crossover_N_mutation(population,fitness,population_No,no_of_Cities,visited_root)
    new_fitness = calcFitness(new_population,no_of_Cities)
    return(new_fitness,new_population)  
    

    
define_epoch = 9
for i in range(0,define_epoch):
    fitness,population = GA_knapsack(population,fitness,population_No,no_of_Cities,visited_root)
#    for j in range(0,population_No):
#        print('Epoch : ',i,' population -> ',j,' : ',population[j])
#    for j in range(0,population_No):
#       print('Epoch : ',i,' Fitness -> ',j,' : ',fitness[j])
    print('Epoch > ',i+1,' ',end = ' ')
    final_result(population,fitness) 

print('\nGA Result:')
final_result(population,fitness)        
print('Actual output : ',[1,3,4,2,5,1],' Cost : ',34)
print('Used Time',time.time() - start_time,'s')
