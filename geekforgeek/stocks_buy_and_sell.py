def stockBuySell( A, n):
        #code here
        res = []
        min_index = 0
        min1 = A[0]
        
        idx=0
        
        for i in range(1,len(A)):
            if A[i] < min1:
                min1 = A[i]
                min_index = i
                idx=i
            else:
                res.append([min_index,i])
                min1 = A[i]
                min_index = i
                idx=i
        print(idx)
a=[7,1,5,3,6,4]
n=6
stockBuySell(a,n)
