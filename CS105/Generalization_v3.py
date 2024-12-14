import pandas as pd
import functions

## This is V3. 
## Generalizations: Age (Version 2), BMI
## Suppressions: None
## Quasi-identifiers: ['age', 'sex', 'region', 'bmi'] 
##---------------------------------------------

# Load the CSV file
data = pd.read_csv("insurance.csv")
data['age'] = pd.to_numeric(data['age'], errors='coerce')

data['age'] = data['age'].apply(functions.generalize_age_2)
data['bmi'] = data['bmi'].apply(functions.generalize_bmi)

# Save the updated data to a new CSV file
generalized_v3_file_path = 'insurance_generalized_v3.csv'
data.to_csv(generalized_v3_file_path, index=False)

generalized_v3_file_path
