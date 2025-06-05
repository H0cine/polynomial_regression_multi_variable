import numpy as np
import matplotlib.pyplot as plt

def polynomial_regression(points, degree):
    x = np.array([point[:-1] for point in points])
    y = np.array([point[-1] for point in points])
    X_poly = np.ones((len(points), 1))

    for i in range(degree):
        for j in range(x.shape[1]):
            X_poly = np.hstack((X_poly, (x[:, j] ** (i + 1)).reshape(-1, 1)))

    coefficients = np.linalg.lstsq(X_poly, y, rcond=None)[0]
    return coefficients

def regression_equation(x_val, coefficients, degree):
    x_val = np.array(x_val)
    result = coefficients[0]
    power = 1
    for i in range(degree):
        for j in range(len(x_val)):
            result += coefficients[power] * (x_val[j] ** (i + 1))
            power += 1
    return result

# === User Input ===
points = []
degree = int(input("Enter the degree of the regression polynomial: "))

choice = ""
while choice != "s":
    i = len(points) + 1
    data = list(map(float, input(f"Enter the {degree} values for point {i} (format: x y): ").split()))
    points.append(data)
    choice = input("Type 's' to stop or any other key to continue: ").lower()

coefficients = polynomial_regression(points, degree)
print(f"Coefficients: {coefficients}")

# === Show Equation ===
equation = "y = "
power = 0
for coef in coefficients:
    if power == 0:
        equation += f"{coef:.2f}"
    else:
        equation += f" + {coef:.2f}x^{power}"
    power += 1
print("The regression polynomial equation is:", equation)

# === Prediction ===
num_features = len(points[0]) - 1
x_pred = list(map(float, input(f"Enter the {num_features} value(s) of x to predict y: ").split()))
y_pred = regression_equation(x_pred, coefficients, degree)
print(f"Predicted result: y = {y_pred:.2f}")

# === Plot (only for 1D input) ===
if num_features == 1 and degree == 2:
    plot_choice = input("Do you want a graph? (yes/YES to confirm): ").lower()
    if plot_choice == "yes":
        x_vals = np.array([p[0] for p in points])
        y_vals = np.array([p[1] for p in points])

        x_range = np.linspace(min(x_vals), max(x_vals), 100)
        y_range = np.array([regression_equation([x], coefficients, degree) for x in x_range])

        plt.scatter(x_vals, y_vals, color='red', label='Data points')
        plt.plot(x_range, y_range, color='blue', label='Polynomial Fit')
        plt.title("Polynomial Regression")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        plt.show()
