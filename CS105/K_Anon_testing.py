import pandas as pd
import numpy as np
from scipy.stats import t, zscore

# Function to calculate k-Anonymity
def calculate_k_anonymity(file_path: str, quasi_identifiers: list) -> int:
    """
    Parameters:
        file_path (str): The path to the CSV file.
        quasi_identifiers (list): A list of column names considered to be quasi-identifiers.

    Returns:
        int: The k-anonymity value of the dataset.
    """
    # Load csv into a pandas df
    data = pd.read_csv(file_path)
    
    # Make sure quasi-identifiers exist (precautionary for edge case)
    for col in quasi_identifiers:
        if col not in data.columns:
            raise ValueError(f"Column '{col}' not found in the dataset.")
    
    # Group by quasi-identifiers and count rows per group
    group_sizes = data.groupby(quasi_identifiers).size()
    
    # Note: k-anonymity value is the size of the smallest group
    k_anonymity = group_sizes.min()
    
    return k_anonymity

# The original k-anonymity value of the dataset
k_anonymity_original = calculate_k_anonymity('insurance.csv', ['age', 'sex', 'bmi', 'region'])
print("Orignial", k_anonymity_original)

# The k-anonymity value of the dataset AFTER generalization (v1)
k_anonymity_generalized_v1 = calculate_k_anonymity('insurance_generalized_v1.csv', ['age', 'sex', 'bmi', 'region'])
print("Generalized (v1)", k_anonymity_generalized_v1)

# The k-anonymity value of the dataset AFTER generalization (v2)
k_anonymity_generalized_v2 = calculate_k_anonymity('insurance_generalized_v2.csv', ['age', 'sex', 'bmi', 'region'])
print("Generalized (v2)", k_anonymity_generalized_v2)

# The k-anonymity value of the dataset AFTER generalization (v3)
k_anonymity_generalized_v3 = calculate_k_anonymity('insurance_generalized_v3.csv', ['age', 'sex', 'bmi', 'region'])
print("Generalized (v3)", k_anonymity_generalized_v3)

# The k-anonymity value of the dataset AFTER generalization (v4)
k_anonymity_generalized_v4 = calculate_k_anonymity('insurance_generalized_v4.csv', ['age', 'sex', 'region', 'bmi'])
print("Generalized (v4)", k_anonymity_generalized_v4)

# The k-anonymity value of the dataset AFTER generalization (v5)
k_anonymity_generalized_v5 = calculate_k_anonymity('insurance_generalized_v5.csv', ['age', 'sex', 'region', 'bmi'])
print("Generalized (v5)", k_anonymity_generalized_v5)

# The k-anonymity value of the dataset AFTER generalization (v6)
k_anonymity_generalized_v6 = calculate_k_anonymity('insurance_generalized_v6.csv', ['age', 'sex', 'region', 'bmi'])
print("Generalized (v6)", k_anonymity_generalized_v6)

# The k-anonymity value of the dataset AFTER generalization (v7)
k_anonymity_generalized_v7 = calculate_k_anonymity('insurance_generalized_v7.csv', ['age', 'sex', 'region', 'bmi'])
print("Generalized (v7)", k_anonymity_generalized_v7)

# The k-anonymity value of the dataset AFTER generalization (v8)
k_anonymity_generalized_v8 = calculate_k_anonymity('insurance_generalized_v8.csv', ['age', 'sex', 'region', 'bmi', 'charges'])
print("Generalized (v8)", k_anonymity_generalized_v8)

# The k-anonymity value of the dataset AFTER generalization (v9)
k_anonymity_generalized_v9 = calculate_k_anonymity('insurance_generalized_v9.csv', ['age', 'sex', 'region', 'bmi', 'charges'])
print("Generalized (v9)", k_anonymity_generalized_v9)

# The k-anonymity value of the dataset AFTER generalization (v10)
k_anonymity_generalized_v10 = calculate_k_anonymity('insurance_generalized_v10.csv', ['age', 'sex', 'region', 'bmi'])
print("Generalized (v10)", k_anonymity_generalized_v10)