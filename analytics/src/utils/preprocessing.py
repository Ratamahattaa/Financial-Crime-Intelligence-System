from pathlib import Path
import pandas as pd


def load_transactions(raw_dir: Path) -> pd.DataFrame:
    raw_dir.mkdir(parents=True, exist_ok=True)
    file_path = raw_dir / "transactions_sample.csv"
    if not file_path.exists():
        raise FileNotFoundError(f"Brak pliku z transakcjami: {file_path}")
    df = pd.read_csv(file_path)
    return df


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["hour"] = df["timestamp"].dt.hour
        df["day_of_week"] = df["timestamp"].dt.dayofweek
    else:
        df["hour"] = 12
        df["day_of_week"] = 0

    if "amount" not in df.columns:
        df["amount"] = 0.0

    return df
