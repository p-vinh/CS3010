# Forward Elimination
def FwdElimination(coeff, const, n):
    for i in range(n-1):
        for j in range(i+1, n):
            mult = coeff[j][i] / coeff[i][i]
            
            for k in range(i, n):
                coeff[j][k] = coeff[j][k] - mult * coeff[i][k]
            const[j] = const[j] - mult * const[i]
    return coeff, const

# Back Substitution
def BackSubst(coeff, const, sol, n):
    sol[n-1] = const[n-1] / coeff[n-1][n-1]
    
    for i in range(n - 1, -1, -1):
        sumC = const[i]
        for j in range(i+1, n):
            sumC = sumC - coeff[i][j] * sol[j]
        sol[i] = sumC / coeff[i][i]
    return sol