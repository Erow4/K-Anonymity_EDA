import pandas as pd
import functions

## This is V2. 
## Generalizations: Age (Version 1), BMI
## Suppressions: None
## Quasi-identifiers: ['age', 'sex', 'region', 'bmi']
##---------------------------------------------

# Load the CSV file
data = pd.read_csv("insurance.csv")
data['age'] = pd.to_numeric(data['age'], errors='coerce')

# Apply the generalizations
data['age'] = data['age'].apply(functions.generalize_age)
data['bmi'] = data['bmi'].apply(functions.generalize_bmi)

# Save the updated dataset
generalized_v2_file_path = 'insurance_generalized_v2.csv'
data.to_csv(generalized_v2_file_path, index=False)

generalized_v2_file_path