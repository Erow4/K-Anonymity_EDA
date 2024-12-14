import pandas as pd
import functions

## This is V10. 
## Generalizations: BMI, charges
## Suppressions: Age, Region, Sex
## Quasi-identifiers: ['age', 'sex', 'region', 'bmi'] 
##---------------------------------------------


# Load the CSV file
data = pd.read_csv("insurance.csv")
data['age'] = pd.to_numeric(data['age'], errors='coerce')

data['bmi'] = data['bmi'].apply(functions.generalize_bmi)
data['charges'] = data['charges'].apply(functions.generalize_charges)
data['region'] = '****'
data['age'] = '****'
data['sex'] = '****'

# Save the updated data to a new CSV file
generalized_v10_file_path = 'insurance_generalized_v10.csv'
data.to_csv(generalized_v10_file_path, index=False)

generalized_v10_file_path
