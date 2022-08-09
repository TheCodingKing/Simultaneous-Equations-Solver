from numpy import matrix
from string import ascii_lowercase as alphabet

unknowns = ["x", "y", "z"]



no_of_variables = int(input("Enter the number of unknowns to solve (upto 3): ").strip())

for n in range(no_of_variables):
    globals()[f"eqn{n + 1}"] = ""


all_constants_list = []
all_coefficients_list = []

for i in range(no_of_variables): # [1:]:
    for j in range(no_of_variables):
        # print(f"i={i}")
        if globals()[f"eqn{j + 1}"] == "":
            globals()[f"eqn{j + 1}"] += (f"{alphabet[i]}{unknowns[i]}")
        else:
            globals()[f"eqn{j + 1}"] += (f" + {alphabet[i]}{unknowns[i]}")

for k in range(no_of_variables): globals()[f"eqn{k + 1}"] += (" = const")


for j in range(no_of_variables):
    print(f"\nEquation {j+1}: {globals()[f'eqn{j+1}']}")
    for k in range(no_of_variables):
        all_coefficients_list.append(int(input(f"{alphabet[k]}: ").strip()))
    all_constants_list.append(int(input("const: ").strip()))


all_constants_matrix = matrix(all_constants_list).reshape(no_of_variables,1)
all_coefficients_matrix = matrix(all_coefficients_list).reshape(no_of_variables,no_of_variables)


inverse_coefficients_matrix = all_coefficients_matrix.getI()
answer = inverse_coefficients_matrix * all_constants_matrix

print("\nSolutions:")
for i in range(no_of_variables):
    print(f"{unknowns[i]} = {answer[i]}")
