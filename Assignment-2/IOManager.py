# Description: This file contains functions to read input and save output
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
        f.write(str(sol[0])) # Root
        f.write(str(sol[1])) # Iterations
        f.write(sol[2]) # Outcome
        f.write("\n")
    print("Output saved to %s" %(fileName))