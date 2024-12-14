import pandas as pd
import functions

## This is V6. 
## Generalizations: Age (Version 2), BMI
## Suppressions: Region, Sex
## Quasi-identifiers: ['age', 'sex', 'region', 'bmi'] 
##---------------------------------------------

# Load the CSV file
data = pd.read_csv("insurance.csv")
data['age'] = pd.to_numeric(data['age'], errors='coerce')

# Apply the function to the 'age' column
data['age'] = data['age'].apply(functions.generalize_age_2)
data['bmi'] = data['bmi'].apply(functions.generalize_bmi)
data['region'] = '****'
data['sex'] = '****'

# Save the updated data to a new CSV file
generalized_v6_file_path = 'insurance_generalized_v6.csv'
data.to_csv(generalized_v6_file_path, index=False)

generalized_v6_file_path
