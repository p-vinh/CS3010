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
            f.write("%0.2f\n" %(sol[i]))
    print("Output saved to %s" %(fileName))