def modifyMatrix(mat) :
    row_flag = False
    col_flag = False
    
    for i in range(0, len(mat)) :
         
        for j in range(0, len(mat)) :
            if (i == 0 and mat[i][j] == 1) :
                row_flag = True
                     
            if (j == 0 and mat[i][j] == 1) :
                col_flag = True
             
            if (mat[i][j] == 1) :
                mat[0][j] = 1
                mat[i][0] = 1
                 
    
    for i in range(1, len(mat)) :
         
        for j in range(1, len(mat) + 1) :
            if (mat[0][j] == 1 or mat[i][0] == 1) :
                mat[i][j] = 1
                 
    
    if (row_flag == True) :
        for i in range(0, len(mat)) :
            mat[0][i] = 1
             
    
    if (col_flag == True) :
        for i in range(0, len(mat)) :
            mat[i][0] = 1
             

def printMatrix(mat) :
     
    for i in range(0, len(mat)) :
        for j in range(0, len(mat) + 1) :
            print( mat[i][j], end = "" )
         
        print()
         
