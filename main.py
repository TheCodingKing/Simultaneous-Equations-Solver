from numpy import matrix
from string import ascii_lowercase as alphabet


def int_input(text, context="coefficient_input"):
    while True:
        try:
            get_input = int(input(text).strip())
            if context == "no_of_vars_input" and get_input not in (1, 2, 3):
                raise IndexError
            return get_input
        except ValueError:
            print("Please enter in integer form.")
        except IndexError:
            print("Sorry, this program only supports from 1-3 variables. Please try again")


unknown_variables = ["x", "y", "z"]  # This script only supports solving upto three unknowns (for now)

no_of_variables = int_input("Enter the number of unknown_variables to solve (upto 3): ", context="no_of_vars_input")


# Dynamically create variables for each relevant equation, which can be shown to the user before entering inputs
for n in range(no_of_variables):
    globals()[f"eqn{n + 1}"] = ""

all_constants_list = []  # A list to store the constant terms of all equations
all_coefficients_list = []  # Stores the coefficients of all variables in order (before converting to matrix)

# Create equations to show the user
for i in range(no_of_variables):
    for j in range(no_of_variables):
        if globals()[f"eqn{j + 1}"] == "":
            globals()[f"eqn{j + 1}"] += f"{alphabet[i]}{unknown_variables[i]}"
        else:
            globals()[f"eqn{j + 1}"] += f" + {alphabet[i]}{unknown_variables[i]}"

# Add a constant term to show the user before input
for k in range(no_of_variables):
    globals()[f"eqn{k + 1}"] += " = const"

# Ask user to input coefficients of each term
for j in range(no_of_variables):
    print(f"\nEquation {j+1}: {globals()[f'eqn{j+1}']}")
    for k in range(no_of_variables):
        all_coefficients_list.append(int_input(f"{alphabet[k]}: "))
    all_constants_list.append(int_input("const: "))

# Create a column vector (matrix form) with constant terms
all_constants_matrix = matrix(all_constants_list).reshape(no_of_variables, 1)

# Create a square matrix of all coefficients before solving system of equations
all_coefficients_matrix = matrix(all_coefficients_list).reshape(no_of_variables, no_of_variables)

# Solve the simultaneous equations/system of equations.
inverse_coefficients_matrix = all_coefficients_matrix.getI()
answer = inverse_coefficients_matrix * all_constants_matrix

# Return values of each relevant variable
print("\nSolutions:")
for i in range(no_of_variables):
    print(f"{unknown_variables[i]} = {answer[i]}")
