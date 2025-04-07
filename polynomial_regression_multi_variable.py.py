import numpy as np

def polynomial_reg(points, degree):
    x = np.array([point[:-1] for point in points])
    y = np.array([point[-1] for point in points])
    X_poly = np.ones((len(points), 1))

    for i in range(degree):
        for j in range(x.shape[1]):
            X_poly = np.hstack((X_poly, (x[:, j] ** (i + 1)).reshape(-1, 1)))

    coefficients = np.linalg.lstsq(X_poly, y, rcond=None)[0]
    
    return coefficients

points = []
choice = ""
degree = int(input("Enter the degree of the regression polynomial: "))

while choice != "s":
    i = len(points) + 1
    data = list(map(float, input(f"Enter the {degree} values for point {i} (separated by space): ").split()))
    points.append(data)
    choice = input("Type 's' to stop or any other key to continue: ").lower()
    
coefficients = polynomial_reg(points, degree)

equation = "y = "
num_features = len(points[0]) - 1

for i, coef in enumerate(coefficients):
    if i == 0:
        equation += f"{coef:.2f}"
    else:
        equation += f" + {coef:.2f}x^{i+1}"

print(f"The regression polynomial equation is: {equation}")

x_pred = list(map(float, input(f"Enter the {num_features} values of x to predict y (separated by space): ").split()))
x_poly_pred = np.ones((1, 1))

for i in range(degree):
    for j in range(len(x_pred)):
        x_poly_pred = np.hstack((x_poly_pred, np.array([[x_pred[j] ** (i + 1)]])))

y_pred = np.dot(x_poly_pred, coefficients)

print(f"Result: y = {y_pred[0]:.2f}")
