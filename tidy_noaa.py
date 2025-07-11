# tidy_noaa.py
import pandas as pd

df = pd.read_csv("central_park_2024_raw.csv")

# Keep only columns you need
df = df[["date", "datatype", "value"]]

# Pivot tall → wide
wide = (
    df
    .assign(date=lambda d: pd.to_datetime(d["date"]).dt.date)
    .pivot_table(index="date", columns="datatype", values="value", aggfunc="first")
    .reset_index()
)

wide.to_csv("central_park_2024_tidy.csv", index=False)
print("Wrote central_park_2024_tidy.csv with shape:", wide.shape)