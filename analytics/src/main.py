from pathlib import Path

from utils.preprocessing import load_transactions, preprocess
from models.anomaly_detector import IsolationForestDetector, LOFDetector
from models.risk_scoring import compute_risk_score
from utils.graph_simulation import build_transaction_graph, draw_graph


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def run_pipeline():
    df = load_transactions(RAW_DIR)
    df = preprocess(df)

    feature_cols = ["amount", "hour", "day_of_week"]

    iforest = IsolationForestDetector(contamination=0.05)
    iforest.fit(df, feature_cols)
    df = iforest.predict(df)

    lof = LOFDetector(contamination=0.05)
    df = lof.fit_predict(df, feature_cols)

    risk_df = compute_risk_score(df)
    print("Top risky entities:")
    print(risk_df.head())

    export_for_power_bi(df, risk_df)

    G = build_transaction_graph(df)
    draw_graph(G)


def export_for_power_bi(df, risk_df):
    transactions_path = PROCESSED_DIR / "transactions_scored.csv"
    risk_path = PROCESSED_DIR / "risk_scores.csv"

    df.to_csv(transactions_path, index=False)
    risk_df.to_csv(risk_path, index=False)

    print(f"\n[EXPORT] Zapisano: {transactions_path}")
    print(f"[EXPORT] Zapisano: {risk_path}")


if __name__ == "__main__":
    run_pipeline()
