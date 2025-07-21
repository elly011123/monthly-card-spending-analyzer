import pandas as pd
from step_1 import IN_DIR

df_raw = pd.read_excel(IN_DIR / "May2025.xlsx",
                       sheet_name="Sheet1", usecols="B:D", skiprows=2)
df_raw