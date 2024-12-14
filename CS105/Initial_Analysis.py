import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Case study: an OLS regression to predict 
# the value of charges from age, bmi, and children


# Load the uploaded CSV file to review its structure
data = pd.read_csv("insurance.csv")

# Define the dependent variable (y) and independent variables (X)
y = data['charges']
X = data[['age', 'bmi', 'children']]
X = sm.add_constant(X)  # Add a constant for the intercept

# Fit the model
model = sm.OLS(y, X).fit()

# Extract residuals and fitted values
residuals = model.resid
fitted = model.fittedvalues

# QQ Plot
sm.qqplot(residuals, line='45', fit=True)
plt.title("QQ Plot of Residuals")
plt.show()

# Residuals vs. Fitted Plot
plt.scatter(fitted, residuals, alpha=0.7)
plt.axhline(0, color='red', linestyle='--', linewidth=1)
plt.title("Residuals vs. Fitted Values")
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.show()

# Box Plot of Charges
plt.boxplot(data['charges'], vert=False, patch_artist=True)
plt.title("Box Plot of Charges")
plt.xlabel("Charges")
plt.show()
