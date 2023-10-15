import IOManager as io


def bisect(func, a, b, n, maxiter=10000, tol=1e-23):
    fa = f(func, n, a)
    fb = f(func, n, b)
    
    if fa * fb >= 0:
        print("Inadequate values for a and b")
        return -1.0
    
    error = b - a
    c = 0
    
    for i in range(maxiter):
        error = error / 2
        c = a + error
        fc = f(func, n, c)
        
        if error < tol or fc == 0:
            print("Root found at %dth iteration" %(i))
            return c
        
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    
    print("Root not found in %d iterations" %(maxiter))
    return c

def newton(func, dfunc, x0, n, maxiter=10000, tol=1e-23, delta=1e-23):
    fx = f(func, n, x0)
    x = 0
    
    for i in range(maxiter):
        fd = f(dfunc, n-1, x0)
        
        if abs(fd) < delta:
            print("Small derivative")
            return x0
        
        d = fx / fd
        x = x0 - d
        fx = f(func, n, x)
        
        if abs(d) < tol:
            print("Algorithm has converged after #{it} iterations!".format(it=i))
            return x
    
    print("Max iterations reached without convergence...")
    return x
        
def secant(func, x0, x1, maxiter=10000, tol=1e-23):
    
    pass

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


def main():
    n, func = io.readFile("Assignment-2\input.pol")
    print(bisect(func, 0, 1, n))
    print(newton(func, df(func, n), 1, n))

if __name__ == "__main__":
    main()