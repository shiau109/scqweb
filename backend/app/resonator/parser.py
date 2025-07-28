import pandas as pd
import numpy as np
import xarray as xr
from pathlib import Path

def parse_resonator_csv(file_path: str) -> dict:
    df = pd.read_csv(file_path, sep=";", comment="#")
    df = df.dropna(axis=1, how="all")  # drop trailing empty columns if any

    df.columns = [col.strip() for col in df.columns]
    col_map = {
        "freq[Hz]": "Freq(Hz)",
        "re:Trc1_S21": "ReS21",
        "im:Trc1_S21": "ImS21"
    }
    df.rename(columns=col_map, inplace=True)

    if not {"Freq(Hz)", "ReS21", "ImS21"}.issubset(df.columns):
        raise ValueError("Missing required columns after parsing")

    return {
        "format": "format_semicolon",
        "frequency": df["Freq(Hz)"].to_numpy(),
        "real": df["ReS21"].to_numpy(),
        "imag": df["ImS21"].to_numpy(),
    }

def parse_resonator_netcdf(file_path: str) -> dict:
    ds = xr.open_dataset(file_path)

    if "s21" not in ds or "frequency" not in ds:
        raise ValueError("Missing 's21' or 'frequency' in the file.")

    freq = ds["frequency"].values
    s21 = ds["s21"].values  # shape: (s_params, frequency)

    if s21.shape[0] != 2:
        raise ValueError(f"Expected 2 s_params (real, imag), got shape {s21.shape}")

    real = s21[0]
    imag = s21[1]

    return {
        "format": "format_netcdf_litevna",
        "frequency": freq,
        "real": real,
        "imag": imag,
    }

def parse_resonator_file(file_path: str) -> dict:
    path = Path(file_path)
    suffix = path.suffix.lower()

    if suffix == ".csv":
        return parse_resonator_csv(file_path)
    elif suffix == ".nc":
        return parse_resonator_netcdf(file_path)
    else:
        raise ValueError(f"Unsupported file format: {suffix}")
