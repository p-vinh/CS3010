import sys
import NaiveGaussElimination as nge
import ScaledPartialPivot

def readFile(file):
    try:
        coeff = []
        const = []
        with open(file, 'r') as f:
            lines = f.readlines()
            n = int(lines[0])
            for i in range(1, len(lines)-1):
                row = lines[i].split()
                coeff.append(list(map(lambda row : float(row), row)))
            lastRow = lines[len(lines)-1].split()
            const = list(map(lambda lastRow : float(lastRow), lastRow))
    except FileNotFoundError:
        print("File not found!")
        exit(0)
    return n, coeff, const

def saveOutput(fileName, sol):
    with open(fileName, 'w') as f:
        for i in range(len(sol)):
            f.write("{:.15g} ".format(sol[i]))
        f.write("\n")
    print("Output saved to %s" %(fileName))

def main(): 
    if len(sys.argv) < 2:
        print("Usage: python gaussian.py [--spp] <input file>")
        exit(1)
    
    spp = False
    name = sys.argv[-1]
    n, coeff, const = readFile(name)
    
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
    saveOutput(name, sol)


if __name__ == '__main__':
    main()