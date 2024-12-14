import pandas as pd
import functions

## This is V1.
## Generalizations: Age (Version 1)
## Suppressions: None
## Quasi-identifiers: ['age', 'sex', 'region', 'bmi'] 
##---------------------------------------------

# Load the CSV file
data = pd.read_csv("insurance.csv")
data['age'] = pd.to_numeric(data['age'], errors='coerce')

# Apply the function to the 'age' column
data['age'] = data['age'].apply(functions.generalize_age)

# Save the updated data to a new CSV file
generalized_v1_file_path = 'insurance_generalized_v1.csv'
data.to_csv(generalized_v1_file_path, index=False)

generalized_v1_file_path
