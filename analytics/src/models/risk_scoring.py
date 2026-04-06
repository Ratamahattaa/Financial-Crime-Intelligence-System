import pandas as pd


def compute_risk_score(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "entity_id" not in df.columns:
        if "sender_id" in df.columns:
            df["entity_id"] = df["sender_id"]
        else:
            df["entity_id"] = "UNKNOWN"

    for col in ["anomaly_iforest_norm", "anomaly_lof_norm"]:
        if col not in df.columns:
            df[col] = 0.0

    agg = df.groupby("entity_id").agg(
        amount=("amount", "sum"),
        tx_count=("entity_id", "count"),
        anomaly_iforest_norm=("anomaly_iforest_norm", "mean"),
        anomaly_lof_norm=("anomaly_lof_norm", "mean"),
    ).reset_index()

    agg["risk_score"] = (
        0.4 * agg["anomaly_iforest_norm"]
        + 0.4 * agg["anomaly_lof_norm"]
        + 0.2 * (agg["amount"] / (agg["amount"].max() + 1e-9))
    )

    agg = agg.sort_values("risk_score", ascending=False)
    return agg
