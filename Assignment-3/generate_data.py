import random

# Generates a random dataset of n points and writes it to a file
def main():
    n = int(input("Enter the number of points: "))
    
    xvalues = [random.uniform(0, 100) for i in range(n)]
    yvalues = [random.uniform(0, 100) for i in range(n)]

    with open("data.txt", "w") as file:
        file.write("\t".join(map(str, xvalues)) + "\n")
        file.write("\t".join(map(str, yvalues)) + "\n")
        


if __name__ == "__main__":
    main()