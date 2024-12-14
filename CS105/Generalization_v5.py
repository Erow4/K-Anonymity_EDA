import pandas as pd
import functions

## This is V5. 
## Generalizations: BMI
## Suppressions: Region, Age
## Quasi-identifiers: ['age', 'sex', 'region', 'bmi'] 
##---------------------------------------------

# Load the CSV file
data = pd.read_csv("insurance.csv")
data['age'] = pd.to_numeric(data['age'], errors='coerce')

data['bmi'] = data['bmi'].apply(functions.generalize_bmi)
data['region'] = '****'
data['age'] = '****'

# Save the updated data to a new CSV file
generalized_v5_file_path = 'insurance_generalized_v5.csv'
data.to_csv(generalized_v5_file_path, index=False)

generalized_v5_file_path
