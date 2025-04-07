# polynomial_regression_multi_variable

# Polynomial Regression with Multiple Variables

This Python script implements polynomial regression for datasets with multiple input variables (features). It allows the user to:

- Input the degree of the polynomial.
- Enter custom training data points via the console.
- Compute the regression coefficients using least squares.
- Predict the output `y` for a new input vector `x`.

## 📌 Features

- Supports multivariate polynomial regression.
- Dynamic user input for both training and prediction.
- Displays the resulting regression equation.
- Simple CLI interface.

## 🧠 How It Works

1. **Input**: User enters the degree of the polynomial.
2. **Data Collection**: User adds points of the form `[x1, x2, ..., xn, y]` where the last value is the target.
3. **Training**: Builds the polynomial feature matrix and computes coefficients using least squares.
4. **Prediction**: User inputs new values for `x`, and the script predicts the corresponding `y`.

## 🚀 Usage

```bash
python polynomial_regression_multi_variable.py
```

Example Interaction:
Enter the degree of the regression polynomial: 2
Enter the 2 values for point 1 (separated by space): 1 2 10
Type 's' to stop or any other key to continue:
Enter the 2 values for point 2 (separated by space): 2 3 20
Type 's' to stop or any other key to continue: s
The regression polynomial equation is: y = 5.00 + 2.00x^2 + 3.00x^3
Enter the 2 values of x to predict y (separated by space): 3 4
Result: y = 37.00

🧾 Requirements:
1-Python 3.x

2-NumPy

Install dependencies (if needed):

```bash
pip install numpy```

📁 File Structure
├── polynomial_regression_multi_variable.py
└── README.md

