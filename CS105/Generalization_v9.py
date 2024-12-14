import pandas as pd
import functions

## This is V9. 
## Generalizations: BMI
## Suppressions: Age, Region, Sex
## Quasi-identifiers: ['age', 'sex', 'region', 'bmi', 'charges'] 
##---------------------------------------------

# Load the CSV file
data = pd.read_csv("insurance.csv")
data['age'] = pd.to_numeric(data['age'], errors='coerce')


data['bmi'] = data['bmi'].apply(functions.generalize_bmi)
data['region'] = '****'
data['age'] = '****'
data['sex'] = '****'


# Save the updated data to a new CSV file
generalized_v9_file_path = 'insurance_generalized_v9.csv'
data.to_csv(generalized_v9_file_path, index=False)

generalized_v9_file_path