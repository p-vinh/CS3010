
# Forward Elimination
def SPPFwdElimination(coeff, const, ind):
    scaling = [i for i in range(len(coeff))]
    
    for i in range(len(coeff)):
        smax = 0
        
        for j in range(len(coeff)):
            smax = max(smax, abs(coeff[i][j])) # Find coefficient wiht the greatest absolute value
        scaling[i] = smax
    
    for k in range(len(coeff)-1):
        rmax = 0
        maxInd = k
        
        for i in range(k, len(coeff)):
            r = abs(coeff[ind[i]][k] / scaling[ind[i]]) # Ratio of coefficient to scaling factor
            
            if r > rmax:
                rmax = r
                maxInd = i
        temp = ind[maxInd]
        ind[maxInd] = ind[k]
        ind[k] = temp
        
        for i in range(k+1, len(coeff)):
            mult = coeff[ind[i]][k] / coeff[ind[k]][k]
            
            for j in range(k, len(coeff)):
                coeff[ind[i]][j] = coeff[ind[i]][j] - mult * coeff[ind[k]][j]
            const[ind[i]] = const[ind[i]] - mult * const[ind[k]]
    
    return coeff, const, ind

def SPPBackSubst(coeff, const, sol, ind):
    n = len(coeff)-1
    sol[n] = const[ind[n]] / coeff[ind[n]][n]
    
    for i in range(n, -1, -1):
        sumC = const[ind[i]]
        
        for j in range(i+1, len(coeff)):
            sumC = sumC - coeff[ind[i]][j] * sol[j]
        sol[i] = sumC / coeff[ind[i]][i]
    
    return sol