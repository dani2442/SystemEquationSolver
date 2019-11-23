import numpy as np
    
"""
Matrix triangularization

@param a Numpy array of the matrix
@param index Index for the recurrent function
@return triangularized matrix
"""
def gauss(a,index=0):
    var=False
    for i in range(index,len(a)):
        if(a[i][index]!=0):
            var=True
            temp=np.copy(a[index])
            a[index]=a[i]
            a[i]=temp
            break
    if(var):
        for i in range(1+index,len(a)):
            a1=a[index][index]
            b1=a[i][index]
            if(b1==0):
                continue
            else:
                coeff=b1/a1
                a[i]-=coeff*a[index]
    if(index+2==len(a) or index+2==len(a[0])):
        return a
    else: 
        return gauss(a,index+1)
     
"""
Rank calculation

@param a Input matrix
@return rank of matrix a
"""
def rango(a):
    a=np.copy(a)
    gauss(a)
    i=0
    j=0
    while(i<len(a)):
        while(a[i][j]==0):
            j+=1
            if(j==len(a[0])):
                return i
        i+=1
        j+=1
    return i
        
"""
Rank calculation for A|B

@param a Coefficient matrix
@param b Constant matrix
@return rank(a|b)
""" 
def rango_ampliada(a,b):
    c=np.concatenate((a,b.T),axis=1)
    return rango(c)

"""
Solution for system of equations

@param a Coefficient matrix
@param b Constant matrix
@return 0 if unique solution or -1 wheather multiple solutions or non-solution 
""" 
def discutir(a,b):
    r1=rango(a)
    r2=rango(np.concatenate((a,b.T),axis=1))
    
    if(r2!=r1):
        return -1
    else:
        return len(a[0])-r1

    
"""
Solve linear system of equation Ax=B

@param a Coefficient matrix
@param b Constant matrix
@return x where ax=b or -1 if discutir(a,b)==-1
"""
def resolver(a,b):
    if(discutir(a,b)==0):
        c=np.concatenate((a,b.T),axis=1)
        gauss(c)
        i=len(c)-1
        x=np.zeros(i+1)
        while(i>=0):
            suma=c[i][-1]
            for j in range(len(c)-1,i,-1):
                suma-=c[i][j]*x[j]
            x[i]=suma/c[i][i]
            i-=1
            
        return x
    else:
        return -1