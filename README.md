# Computor - Polynomial Equation Solver
<img src="https://github.com/Anastasiia-Ni/computor_v1/blob/main/assets/SubjExample.png" width="500">

## About the project
This Python program is designed to solve polynomial equations of the second degree or lower. 

It showcases the following functionalities:

**Mandatory part**
- Takes a formula in the form of ```"5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"```
- Displaying the equation in its reduced form
- Determining the degree of the equation
- Shows the solutions and the discriminant's polarity if applicable

**Bonus part**
- Capability to add formulas like ```"5 + 4 * X + X^2= X^2"```
- Manage entry mistakes (vocabulary and syntax)
- Display the intermediate steps
- Presents solutions as irreducible fractions (for integer numbers)

Additionally, the program supports solving equations of the third degree.

```"6 * X^1 - 4 * X^0 = 14 * X^0"```

<img src="https://github.com/Anastasiia-Ni/computor_v1/blob/main/assets/Linear.png" width="500">

```"12 * X^2 = -1 * X^0 - 7 * X^1"```

<img src="https://github.com/Anastasiia-Ni/computor_v1/blob/main/assets/Quadratic.png" width="500">

```"2 * X^3 + 9 * X^2 + 13 * X^1 + 6 * X^0 = 0"```

<img src="https://github.com/Anastasiia-Ni/computor_v1/blob/main/assets/%D0%A1ubic.png" width="500">


## Introduction
### Algorithm
1. Check the formula for entry mistakes.
2. Parse and create a dictionary {"x0": [], "x1": [], "x2": [], "x3": []}, where values for each key are added to lists. This is done for displaying the formula in its complete form.
3. Sum all values in each list, and the dictionary takes the form {"x0": 0, "x1": 0, "x2": 0, "x3": 0} for further calculations.
4. Find the polynomial - in the dictionary, the first non-zero value from the end is chosen. Choose a solution method based on the polynomial.
5. Implement solution methods based on the provided code.

### Solution Methods
#### Addition of Monomials
The `addition_monomials` function checks if the equation is false or an identity and prints the appropriate message.

#### Linear Equation
The `solve_linear_equation` function solves and prints the result for a linear equation.

#### Quadratic Equation
- The `solve_quadratic_equation` function calculates the discriminant and determines the method for further solution.
- It includes methods for when the discriminant is zero, positive, or negative.

#### Cubic Equation
- Find coefficients using the Vieta's method for discriminant calculation.
- Calculate the discriminant and determine the method for further solution.
- Determine the method for further solution based on the discriminant.

## Specifications
- Language: Python 3.6.9
- Programs:
  - computor.py

## Installation
```
$ git clone git@github.com:Anastasiia-Ni/computor_v1
$ cd computor_v1
```

## Usage
To use the program, provide a polynomial equation as a command-line argument:

```
$ python computor.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
```
