from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
from step_1 import OUT_DIR
from step_4_2 import load_data

def custom_autopct(pct, total):
    real_val = int(pct / 100 * total)
    return f"${real_val:,}\n({pct:.1f}%)"


df_raw = load_data()
labels, values = df_raw["Categories"], df_raw["Total Amount"]

sns.set_theme(context="poster", font="Malgun Gothic")
fig, ax = plt.subplots(figsize=(16, 9), dpi=100)
ax.pie(
    values,
    textprops=dict(color="white", size=20),
    startangle=90,
    autopct=lambda pct: custom_autopct(pct, sum(values)),
)
ax.legend(labels, loc="center left", bbox_to_anchor=(1, 0.5))
fig.suptitle("Summer 2025 Credit Card Statement")
fig.savefig(OUT_DIR / f"{Path(__file__).stem}.png", bbox_inches="tight")
