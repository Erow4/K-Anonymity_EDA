import pandas as pd

def get_csv_schema(file_path):
    df = pd.read_csv(file_path)
    return df.dtypes

schema1 = get_csv_schema("insurance.csv")
print("Original Schema: ", schema1)

schema5 = get_csv_schema("insurance_generalized_v5.csv")
print("Version 5 Schema: ", schema5)

schema8 = get_csv_schema("insurance_generalized_v8.csv")
print("Version 8 Schema: ", schema8)

