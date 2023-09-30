import IOManager as io
import argparse as ap
import NaiveGaussElimination as nge
import ScaledPartialPivot as spp

def main():
    parser = ap.ArgumentParser()
    parser.add_argument('--spp', help="Scaled Partial Pivoting", action="store_true")
    parser.add_argument('--file', help="Input file name")
    args = parser.parse_args()
    
    if args.file:
        n, coeff, const = io.readFile(args.file)
    else:
        print("Input file not specified!")
        exit(0)
        
    sol = [0 for i in range(len(const))]
    
    if args.spp:
        ind = [i for i in range(len(coeff))]
        
        coeff, const, ind = spp.SPPFwdElimination(coeff, const, ind, n)
        sol = spp.SPPBackSubst(coeff, const, sol, ind, n)
    else:
        coeff, const = nge.FwdElimination(coeff, const, n)
        sol = nge.BackSubst(coeff, const, sol, n)
    io.saveOutput("sys1.sol", sol)


if __name__ == '__main__':
    main()