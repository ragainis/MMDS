# -*- coding: utf-8 -*-
"""

"""
from copy import deepcopy

# Create matrix with col and row
def cmatrix(col, row):
    #col, row should be positive whole integers
    empty_matrix = [[float(0) for i in range(row)] for j in range(col)]
    return empty_matrix

# Create vector with equal probabilities for each row
def cvector(col):
    vector = [1/col for i in range(col)]
    return vector
    
# Update matrix with value in defined location at col, row. Returns updated matrix
def umatrix(matrix, row, col, value):
    #Check row and col are within matrix
    #Check value is integer
    updated_matrix = deepcopy(matrix)
    updated_matrix[row][col] = float(value)
    return updated_matrix
  
# Apply taxation effect on initial matrix table
def tax_matrix(matrix, tax):
    result = matrix
    col1 = len(result)
    row1 = len(result[0])
    for i in range(col1):
        for j in range(row1):
            result[i][j] = result[i][j] * float(tax)
    return result
    
def iter_multip(matrix, vector, iteration,taxa):   
    # Calculate new probability vector of PageRank after one iteration
    result_it = matrix
    vectorCC = vectorC
#    print (vectorCC)
    col1 = len(result_it)
    row1 = len(result_it[0])
    # Create empty vector to store iteration results
    vectorFF = [0 for i in range(row1)]

    while iteration >= 1:
      
        for i in range(col1):
            temp = [0,0,0] 
            for j in range(row1):
                temp[j] = result_it[i][j] * vectorCC[j]
            vectorFF[i] = round((sum(temp) + (1-taxa)/col1),5)
        vectorCC = deepcopy(vectorFF)
        iteration = iteration - 1
    return vectorFF
##### END OF FORMULA DEFINITION######
vectorC = cvector(3)
##MMDS Exercise 1#####  
# Create initial vector of equal probabilities
vectorC1 = cvector(3)
#print (vectorC)

# Create initial empty matrix
resultC1 = cmatrix(3,3)
#print(resultC)

# Update empty matrix with the values
resultU11 = umatrix(resultC1, 1, 0, 0.5)
resultU12 = umatrix(resultU11, 2, 0, 0.5)
resultU13 = umatrix(resultU12, 2, 1, 1)
resultU14 = umatrix(resultU13, 2, 2, 1)

#print('Updated matrix is ' + str(resultU4))

# Apply taxation to the updated matrix
taxedMatrix1 = tax_matrix(resultU14, 0.7)
print(str('\n') + 'Taxed matrix 1 is ' + str(taxedMatrix1)+str('\n'))

ITM1 = iter_multip(taxedMatrix1, vectorC1, 30, 0.7)
print('ITM1 is ' + str(ITM1))
###END Exercise 1##### 

##MMDS Exercise 2#####   
# Create initial vector of equal probabilities
vectorC2 = cvector(3)
#print (vectorC)

# Create initial empty matrix
resultC2 = cmatrix(3,3)
#print(resultC)

# Update empty matrix with the values
resultU21 = umatrix(resultC2, 0, 2, 1)
resultU22 = umatrix(resultU21, 1, 0, 0.5)
resultU23 = umatrix(resultU22, 2, 0, 0.5)
resultU24 = umatrix(resultU23, 2, 1, 1)

#print('Updated matrix is ' + str(resultU4))

# Apply taxation to the updated matrix
taxedMatrix2 = tax_matrix(resultU24, 0.85)
print(str('\n') + 'Taxed matrix 2 is ' + str(taxedMatrix2)+str('\n'))

ITM2 = iter_multip(taxedMatrix2, vectorC2, 30, 0.85)
print('ITM2 is ' + str(ITM2))
###END Exercise 2##### 

##MMDS Exercise 3   
# Create initial vector of equal probabilities
vectorC3 = cvector(3)
#print (vectorC)

# Create initial empty matrix
resultC3 = cmatrix(3,3)
#print(resultC)

# Update empty matrix with the values
resultU31 = umatrix(resultC3, 0, 2, 1)
resultU32 = umatrix(resultU31, 1, 0, 0.5)
resultU33 = umatrix(resultU32, 2, 0, 0.5)
resultU34 = umatrix(resultU33, 2, 1, 1)

#print('Updated matrix is ' + str(resultU4))

# Apply taxation to the updated matrix
taxedMatrix3 = tax_matrix(resultU34, 1)
print(str('\n') + 'Taxed matrix 3 is ' + str(taxedMatrix3)+str('\n'))

ITM3 = iter_multip(taxedMatrix3, vectorC3, 4, 1)
print('ITM3 is ' + str(ITM3))
####END Exercise 3#####    
