import IOManager as io
import sys
import NaiveGaussElimination as nge
import ScaledPartialPivot

def main(): 
    if len(sys.argv) < 2:
        print("Usage: python gaussian.py [--spp] <input file>")
        exit(1)
    
    spp = False
    name = sys.argv[-1]
    n, coeff, const = io.readFile(name)
    
    if len(sys.argv) == 3 and sys.argv[1] == "--spp":
        spp = True
    
    sol = [0 for i in range(n)]
    
    if spp:
        ind = [i for i in range(n)]
        
        coeff, const, ind = ScaledPartialPivot.SPPFwdElimination(coeff, const, ind, n)
        sol = ScaledPartialPivot.SPPBackSubst(coeff, const, sol, ind, n)
    else:
        coeff, const = nge.FwdElimination(coeff, const, n)
        sol = nge.BackSubst(coeff, const, sol, n)
    name = name.replace(".lin", ".sol")
    io.saveOutput(name, sol)


if __name__ == '__main__':
    main()