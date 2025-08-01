from pathlib import Path
import pandas as pd
from step_1 import OUT_DIR
from step_2_2 import OUT_2_2


OUT_3_2 = OUT_DIR / f"{Path(__file__).stem}.xlsx"

if __name__ == "__main__":
    df_raw = pd.read_excel(OUT_2_2)
    df_raw["Month of Transaction"] = df_raw["Date of Transaction"].astype(str).str.slice(0, 7)
    df_pivot = pd.pivot_table(df_raw, index="Categories", columns="Month of Transaction", 
                              values="Amount", aggfunc="sum")

    df_pivot["Total Amount"] = df_pivot.sum(axis=1)

    df_sort = df_pivot.sort_values("Total Amount", ascending=False)
    df_reindex = df_sort.reset_index()
    df_reindex.to_excel(OUT_DIR / f"{Path(__file__).stem}.xlsx", index=False, sheet_name="Total Amount per Categories")