import pandas as pd
from step_2_2 import OUT_2_2

df_raw = pd.read_excel(OUT_2_2)
df_pivot_1 = pd.pivot_table(df_raw, index="Categories", values="Amount", aggfunc="sum")
df_pivot_1

df_raw["Month of Transaction"] = df_raw["Date of Transaction"].astype(str).str.slice(0, 7)
df_raw

df_pivot_2 = pd.pivot_table(df_raw, index="Categories", columns="Month of Transaction", values="Amount", aggfunc="sum")
df_pivot_2["Total Amount"] = df_pivot_2.sum(axis=1)
df_pivot_2

df_sort = df_pivot_2.sort_values("Total Amount", ascending=False)
df_sort

df_reindex = df_sort.reset_index()
df_reindex

from pathlib import Path
from step_1 import IN_DIR , OUT_DIR

df_reindex.to_excel(OUT_DIR / f"{Path(__file__).stem}.xlsx", index=False, sheet_name="Total Amount per Categories")