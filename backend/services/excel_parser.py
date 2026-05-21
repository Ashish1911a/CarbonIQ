import pandas as pd

file_path = "data/GHG.xlsx"


all_sheets = pd.read_excel(
    file_path,
    sheet_name=None
)

print("Loaded Sheets:")
print(all_sheets.keys())


def standardize_columns(df):

    df.columns = [
        col.strip().lower().replace(" ", "_")
        for col in df.columns
    ]

    return df


normalized_records = []

for sheet_name, df in all_sheets.items():

    df = standardize_columns(df)

    print(f"\nProcessing Sheet: {sheet_name}")
    print(df.columns)

    for _, row in df.iterrows():

        record = {

            "scope": sheet_name,

            "activity": row.get("activity", None),

            "quantity": row.get("quantity", 0),

            "unit": row.get("unit", None),

            "factor": row.get("factor", 0),

            "emissions": row.get("emissions", 0)
        }

        normalized_records.append(record)

normalized_df = pd.DataFrame(normalized_records)

print("\nFinal Standardized Data:")
print(normalized_df.head())


normalized_df.to_csv(
    "normalized_ghg_data.csv",
    index=False
)

print("\nNormalization Complete")