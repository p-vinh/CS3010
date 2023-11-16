import sys
import time

# Calculates the coefficients of the Newton polynomial
def Coeff(xs, ys, cs):
    n = len(xs) - 1

    for i in range(n + 1):
        cs[i] = ys[i]

    for j in range(1, n + 1):
        for i in range(n, j - 1, -1):
            cs[i] = (cs[i] - cs[i - 1]) / (xs[i] - xs[i - j])
    return cs

# Evaluates the polynomial at a given value using Newton's method
def evalNewton(xs, cs, z):
    n = len(xs) - 1
    result = cs[n]

    for i in range(n - 1, -1, -1):
        result = result * (z - xs[i]) + cs[i]

    return result

# Retrieves user input with either 'q' or a value to evaluate the polynomial
def get_value():
    while True:
        z = input("| Enter the value to evaluate polynomial | 'q' to quit) | ")
        if z.lower() == 'q':
            return "Quit"
        try:
            return z
        except ValueError:
            print("Invalid input. Valid floating-point values only.")

# Reads data from a file and returns two lists of x and y values
def read_data(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    x_string = lines[0].split()
    y_string = lines[1].split()
    
    x_values = []
    y_values = []
    
    for x in x_string:
        x_values.append(float(x))
        
    for y in y_string:
        y_values.append(float(y))

    return x_values, y_values

def main(file_path):
    try:
        x_values, y_values = read_data(file_path)
    except FileNotFoundError:
        print("File not found. Exiting.")
        return
    except ValueError:
        print("Invalid data format in the file. Exiting.")
        return

    n = [0] * len(x_values)

    start_time = time.time()
    coeffs = Coeff(x_values, y_values, n)
    
    interpolation_time = time.time() - start_time
    print(f"Interpolation computed in {interpolation_time} seconds.")

    while True:
        z = get_value()
        if z == "Quit":
            return

        start_time = time.time()
        result = evalNewton(x_values, coeffs, float(z))
        
        evaluation_time = time.time() - start_time
        print(f"Polynomial evaluated in {evaluation_time} seconds.")

        print(f"Result: {result}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py file_path")
    else:
        file_path = sys.argv[1]
        main(file_path)