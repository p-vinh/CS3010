
# Forward Elimination
def SPPFwdElimination(coeff, const, ind, n):
    scaling = [i for i in range(n)]
    
    for i in range(n):
        smax = 0
        
        for j in range(n):
            smax = max(smax, abs(coeff[i][j])) # Find coefficient wiht the greatest absolute value
        scaling[i] = smax
    
    for k in range(n-1):
        rmax = 0
        maxInd = k
        
        for i in range(k, n):
            r = abs(coeff[ind[i]][k] / scaling[ind[i]]) # Ratio of coefficient to scaling factor
            
            if r > rmax:
                rmax = r
                maxInd = i
        temp = ind[maxInd]
        ind[maxInd] = ind[k]
        ind[k] = temp
        
        for i in range(k+1, n):
            mult = coeff[ind[i]][k] / coeff[ind[k]][k]
            
            for j in range(k, n):
                coeff[ind[i]][j] = coeff[ind[i]][j] - mult * coeff[ind[k]][j]
            const[ind[i]] = const[ind[i]] - mult * const[ind[k]]
    
    return coeff, const, ind

def SPPBackSubst(coeff, const, sol, ind, n):
    sol[n-1] = const[ind[n-1]] / coeff[ind[n-1]][n-1]
    
    for i in range(n-1, -1, -1):
        sumC = const[ind[i]]
        
        for j in range(i+1, n):
            sumC = sumC - coeff[ind[i]][j] * sol[j]
        sol[i] = sumC / coeff[ind[i]][i]
    
    return sol