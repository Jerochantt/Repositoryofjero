#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 10:23:22 2021

@author: jeromechantiantze
"""
import matplotlib.pyplot as plt
import numpy as np
te = np.arange(0.1,4.1,0.1)


# function of the swapping mechanism 
def Loop1(C):
                
                # Selecting 2 particles from the Matrix 
                CoodX1 = np.random.randint(0,10) 
                CoodY1 = np.random.randint(0,10) 
                
                CoodX2 = np.random.randint(0,10)
                CoodY2 = np.random.randint(0,10)
                
                
                
                # Ensuring it's not the same element
                if C[CoodX1,CoodY1] != C[CoodX2,CoodY2]:
                    E1 = C[CoodX1,CoodY1]
                    E2 = C[CoodX2,CoodY2]
                    
                else:
                    CoodX1 = np.random.randint(0,10)
                    CoodY1 = np.random.randint(0,10)
                    
                    CoodX2 = np.random.randint(0,10)
                    CoodY2 = np.random.randint(0,10)
                    
                
                    
                    E1 = C[CoodX1,CoodY1]
                    E2 = C[CoodX2,CoodY2]
                  
                
                
                
                # Labelling the shifts
                CoodX1U = CoodX1 - 1
                CoodX1D = CoodX1 + 1
                CoodX2U = CoodX2 - 1
                CoodX2D = CoodX2 + 1 
                
                CoodY1L = CoodY1 - 1
                CoodY1R = CoodY1 + 1 
                CoodY2L = CoodY2 - 1
                CoodY2R = CoodY2 + 1
                
                
                #Boundary Counditions:
                
                if CoodX1 == 0:
                    CoodX1U = 9
                if CoodX1 == 9:
                    CoodX1D  = 0
                if CoodX2 == 0:
                    CoodX2U  = 9
                if CoodX2 == 9:
                    CoodX2D  = 0
                
                
                if CoodY1 == 0:
                    CoodY1L  = 9
                if CoodY1 == 9:
                    CoodY1R  = 0
                if CoodY2 == 0:
                    CoodY2L  = 9
                if CoodY2 == 9:
                    CoodY2R  = 0
                    
                
                    
                    
                    
                    
                    
                #Calculating Energy for Particle E1
                
                E1Left = C[CoodX1,CoodY1L]
                if E1Left == E1:
                    EL1 = 0
                else:
                    EL1 = 1
                    
                E1Right = C[CoodX1,CoodY1R]
                if E1Right == E1:
                    ER1 = 0
                else:
                    ER1 = 1
                    
                E1Up = C[CoodX1U, CoodY1]
                if E1Up == E1:
                    EU1 = 0
                else:
                    EU1 = 1    
                
                E1Down = C[CoodX1D, CoodY1]
                if E1Down == E1:
                    ED1 = 0
                else:
                    ED1 = 1    
                    
                ET1 = EL1 +  ER1 +  EU1   + ED1
               
                    
                
                
                #Calculating Energy for Particle E2:   
                    
                    
                E2Left = C[CoodX2,CoodY2L]
                if E2Left == E2:
                    EL2 = 0
                else:
                    EL2 = 1
                    
                E2Right = C[CoodX2,CoodY2R]
                if E2Right == E2:
                    ER2 = 0
                else:
                    ER2 = 1
                    
                E2Up = C[CoodX2U, CoodY2]
                if E2Up == E2:
                    EU2 = 0
                else:
                    EU2 = 1    
                
                E2Down = C[CoodX2D, CoodY2]
                if E2Down == E2:
                    ED2 = 0
                else:
                    ED2 = 1    
                    
                ET2 = EL2 +  ER2 +  EU2   + ED2
            
          
                
                # Calculating Total E before swap:
                
                TEbefore = ET1 + ET2
             
                
           
                
                # Swopping the 2 chosen ones
                #print(C)
                E1 = C[CoodX1,CoodY1]
                E2 = C[CoodX2,CoodY2]
                
                E1 = C[CoodX2,CoodY2]
                E2 = C[CoodX1,CoodY1]
                
                C[CoodX1,CoodY1], C[CoodX2,CoodY2] = C[CoodX2,CoodY2], C[CoodX1,CoodY1]
                
              
                
                
                # Calculating the Energy of the chosen ones at their new locations
                # Calculating Energy of Particle 1
                
                
                E1Left = C[CoodX1,CoodY1L]
                if E1Left == E1:
                    EL1 = 0
                else:
                    EL1 = 1
                    
                E1Right = C[CoodX1,CoodY1R]
                if E1Right == E1:
                    ER1 = 0
                else:
                    ER1 = 1
                    
                E1Up = C[CoodX1U, CoodY1]
                if E1Up == E1:
                    EU1 = 0
                else:
                    EU1 = 1    
                
                E1Down = C[CoodX1D, CoodY1]
                if E1Down == E1:
                    ED1 = 0
                else:
                    ED1 = 1    
                    
                ET1 = EL1 +  ER1 +  EU1   + ED1
           
                    
                
                
                # Calculating Energy for Particle E2:   
                    
                    
                E2Left = C[CoodX2,CoodY2L]
                if E2Left == E2:
                    EL2 = 0
                else:
                    EL2 = 1
                    
                E2Right = C[CoodX2,CoodY2R]
                if E2Right == E2:
                    ER2 = 0
                else:
                    ER2 = 1
                    
                E2Up = C[CoodX2U, CoodY2]
                if E2Up == E2:
                    EU2 = 0
                else:
                    EU2 = 1    
                
                E2Down = C[CoodX2D, CoodY2]
                if E2Down == E2:
                    ED2 = 0
                else:
                    ED2 = 1    
                    
                ET2 = EL2 +  ER2 +  EU2   + ED2
       
                
                # Calculating Total E after swap:
                
                TEafter = ET1 + ET2
           
                
                #stay swapped if energy after < energy before 
                if TEbefore >= TEafter: 
                    C = C
        
                else:
                    Prob = np.exp(-(TEafter-TEbefore)/Temperature)
                    
                    # Generate random Prob:
                    import random
                    Frac = (random.randint(1,100))/100
                    
               
                    
                    if Frac < Prob:
                        C = C
                     
                    else: 
                        C[CoodX2,CoodY2], C[CoodX1,CoodY1] = C[CoodX1,CoodY1], C[CoodX2,CoodY2]

SpecificHeat_list = np.array([])
AverageEn_list = np.array([])
for Temperature in te:
    print("")
    print("Temperature is",Temperature)
    Macroenergysum = 0
    Macroenergyaquaresum = 0 

    
    
    # Making Matrix of zeros
    N = np.random.randint(1, size = [5,10])
    # Making Matrix of ones
    M = np.ones([5,10])
    # Combining the 2 Matrices
    C = np.concatenate((N,M))
    # Shuffle all elements in the matrix
    for i in range(10):
        np.random.shuffle(C[:,i])
    
    for p in range(20000):
        Loop1(C)
    # 20 rounds of 1000 MC runs
    for k in range(20):
          
        Macroenergy = 0
        for m in range(1000):
            Loop1(C)
        
        # Calculate macroenergy     
        for i in range(10):
                for j in range(10):
                    #Calculate individual particle energy 
                    ChosenP = C[i,j] 
                    
                    
                    PUindex1 = i - 1
                    PDindex1 = i + 1
                    PLindex2 = j - 1
                    PRindex2 = j + 1
                    
                    
                    #boundary conditions
                    if i == 0:
                        PUindex1 = 9
                        
                    if i == 9:
                        PDindex1 = 0 
                        
                    if j == 0:
                        PLindex2 = 9 
                    
                    if j == 9:
                        PRindex2 = 0
                       
                    
                    #Calculating energy of chosen particle
                    
                    if C[PUindex1,j] == C[i,j]:
                        EupC = 0
                    else: 
                        EupC = 1
                        
                    if C[PDindex1,j] == C[i,j]:
                        EdownC = 0
                    else:
                        EdownC = 1
                    
                    if C[i,PLindex2] == C[i,j]:
                        EleftC = 0 
                    else: 
                        EleftC = 1
                        
                    if C[i,PRindex2] == C[i,j]:
                        ErightC = 0 
                    else: 
                        ErightC = 1
                        
                    
                    ETOTC = EupC + EdownC + EleftC + ErightC
                    
                       
                    Macroenergy = Macroenergy + ETOTC
       
            
        Macroenergysum = Macroenergysum + Macroenergy
        #Calculate sum of macroenergy squares
        Macroenergyaquaresum = Macroenergyaquaresum + Macroenergy**2
    
    #Calculate average macroenergy
    Averagemacroenergy = Macroenergysum/20
    print("Average macroenergy is",Averagemacroenergy)
    
    #Calculate specific heat
    Specificheatsquare = ((Macroenergyaquaresum/20)-((Averagemacroenergy)**2))/(Temperature**2)
    Specificheat = np.sqrt(Specificheatsquare)
    print("Specificheat is",Specificheat)
    
    #Displaying matrix figure
    fig1, ax1 = plt.subplots()
    ax1.imshow(C)
    
    #Calculating rho and compiling them into a list 
    Rholist = np.array([])
    for i in range(10):
        for j in range(10):
            
            
            PUindex1 = i - 1
            PDindex1 = i + 1
            PLindex2 = j - 1
            PRindex2 = j + 1
            
            #boundary conditions
            if i == 0:
                PUindex1 = 9
                        
            if i == 9:
                PDindex1 = 0 
                        
            if j == 0:
                PLindex2 = 9 
                    
            if j == 9:
                PRindex2 = 0
            
            #Calculating Rho
            rho_ij = C[i,j] + C[PUindex1,PLindex2] + C[PUindex1,j] + C[PUindex1,PRindex2] + C[i,PLindex2] + C[i,PRindex2] + C[PDindex1,PLindex2] + C[PDindex1,j] + C[PDindex1,PRindex2]
            #appending rholist every rounf
            Rholist = np.append(Rholist,[rho_ij])
    #Histogram of Rho    
    fig2,ax2 = plt.subplots()
    ax2.hist(Rholist)
    
    SpecificHeat_list = np.append(SpecificHeat_list,[Specificheat])
    AverageEn_list = np.append(AverageEn_list,Averagemacroenergy)

fig3, ax3 = plt.subplots()   
fig4, ax4 = plt.subplots() 
ax3.plot(te,AverageEn_list)
ax4.plot(te,SpecificHeat_list)



    
    
    
                
                
                
                