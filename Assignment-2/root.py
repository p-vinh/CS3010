import IOManager as io
import argparse


HYBRID_BISECTION_ITERATION = 8
IEE754_EPSILON = 2 ** -23
DELTA = 0.00001

def bisect(func, a, b, n, maxiter=10000, tol=IEE754_EPSILON):
    fa = f(func, n, a)
    fb = f(func, n, b)
    
    if fa * fb >= 0:
        print("Inadequate values for a and b")
        return [-1.0, 0, False]
    
    error = b - a
    c = 0
    
    for i in range(maxiter):
        error = error / 2
        c = a + error
        fc = f(func, n, c)
        
        if abs(error) < tol or fc == 0:
            print("Root found at %dth iteration" %(i))
            return [c, i, True]
        
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    
    print("Root not found in %d iterations" %(maxiter))
    return [c, maxiter, False]

def newton(func, dfunc, x, n, maxiter=10000, tol=IEE754_EPSILON, delta=DELTA):
    fx = f(func, n, x)
    x = 0
    
    for i in range(maxiter):
        fd = f(dfunc, n-1, x)
        
        if abs(fd) < delta:
            print("Small derivative")
            return [x, i, False]
        
        d = fx / fd
        x = x - d
        fx = f(func, n, x)
        
        if abs(d) < tol:
            print("Algorithm has converged after #{it} iterations!".format(it=i))
            return [x, i, True]
    
    print("Max iterations reached without convergence...")
    return [x, maxiter, False]
        
def secant(func, a, b, n, maxiter=10000, tol=IEE754_EPSILON):
    fa = f(func, n, a)
    fb = f(func, n, b)
    
    if abs(fa) > abs(fb):
        a, b = b, a
        fa, fb = fb, fa
    
    for i in range(maxiter):
        if abs(fa) > abs(fb):
            a, b = b, a
            fa, fb = fb, fa
        
        d = (b - a) / (fb - fa)
        b = a
        fb = fa
        d *= fa
        
        if abs(d) < tol:
            print("Algorithm has converged after #{it} iterations!".format(it=i))
            return [a, i, True]

        a = a - d
        fa = f(func, n, a)
        
    print("Maximum number of iterations reached!")
    return [a, maxiter, False]

def hybrid(func, x0, x1, n, maxiter=10000, tol=IEE754_EPSILON):
    iterationCounter = 0
    root = 0

    x, iterationCounter, _ = bisect(func, x0, x1, n, HYBRID_BISECTION_ITERATION)
    newtIterationCounter = 0
    if (iterationCounter < maxiter):
        print("Switching to Newton Method")
        root, newtIterationCounter, outcome = newton(func, df(func, n), x, n, maxiter - iterationCounter)
    iterationCounter += newtIterationCounter
    
    return [root, iterationCounter, outcome]

def f(func, n, x):
    result = 0
    for i in range(n, -1, -1):
        result += func[n - i] * (x ** i)
    return result

def df(func, n):
    result = []
    for i in range(n, 0, -1):
        result.append(func[n - i] * i)
    return result

def readFile(file):
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
            n = int(lines[0].strip())
            func = [float(i) for i in lines[1].strip().split()]
    except FileNotFoundError:
        print("File not found!")
        exit(0)
    return n, func

def saveOutput(fileName, sol):
    with open(fileName, 'w') as f:
        for i in sol: f.write(str(i) + " ")
        f.write("\n")
    print("Output saved to %s" %(fileName))

def main():
    parser = argparse.ArgumentParser()
    
    polyFunc = parser.add_argument_group("Finding roots of polynomial functions")
    polyFunc.add_argument("-newt", action="store_true", help="Use Newton's method with initial point x0", required=False)
    polyFunc.add_argument("-sec", action="store_true", help="Use Secant method with initial points x0 and x1", required=False)
    polyFunc.add_argument("-hybrid", action="store_true", help="Use Hybrid method with initial points x0 and x1", required=False)

    points = parser.add_argument_group("Points")
    points.add_argument("initP", type=float, help="initial point")
    points.add_argument("initP2", type=float, help="initial point 2", nargs='?')
    
    parser.add_argument("filename", help="input file name")
    parser.add_argument("-maxIt", metavar="# of Max Iterations", type=int, default=10000)
    
    args = parser.parse_args()
    print(args._get_args)
    
    if args.sec and args.initP is None and args.initP2 is None:
        print("Invalid number of arguments")
        return -1
    elif args.hybrid and args.initP is None and args.initP2 is None:
        print("Invalid number of arguments")
        return -1
    elif args.newt:
        if args.initP is None or args.initP2 is not None:
            print("Invalid Arguments")
            return -1
    
    n, func = io.readFile(args.filename)
    
    if args.sec:
        x0 = args.initP
        x1 = args.initP2
        print("Using Secant method")
        output = secant(func, x0, x1, n, args.maxIt)
    elif args.newt:
        x0 = args.initP
        print("Using Newton's method")
        output = newton(func, df(func, n), x0, n, args.maxIt)
    elif args.hybrid:
        x0 = args.initP
        x1 = args.initP2
        print("Using hybrid method")
        output = hybrid(func, x0, x1, n, args.maxIt)
    else:
        if args.initP2 is None:
            print("Invalid number of arguments")
            return -1
        x0 = args.initP
        x1 = args.initP2
        print("Using bisection method")
        output = bisect(func, x0, x1, n, args.maxIt)
    
    filename = args.filename.replace(".pol", ".sol")
    io.saveOutput(filename, output)
    
if __name__ == "__main__":
    main()