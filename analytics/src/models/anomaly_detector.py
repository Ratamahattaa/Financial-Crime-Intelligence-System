import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor


class IsolationForestDetector:
    def __init__(self, contamination: float = 0.05, random_state: int = 42):
        self.contamination = contamination
        self.random_state = random_state
        self.model = IsolationForest(
            contamination=self.contamination,
            random_state=self.random_state,
        )

    def fit(self, df: pd.DataFrame, feature_cols: list[str]) -> None:
        self.model.fit(df[feature_cols])

    def predict(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        scores = self.model.decision_function(df[self.model.feature_names_in_])
        df["anomaly_iforest_raw"] = -scores
        df["anomaly_iforest_norm"] = (
            df["anomaly_iforest_raw"] - df["anomaly_iforest_raw"].min()
        ) / (df["anomaly_iforest_raw"].max() - df["anomaly_iforest_raw"].min() + 1e-9)
        return df


class LOFDetector:
    def __init__(self, contamination: float = 0.05, n_neighbors: int = 20):
        self.contamination = contamination
        self.n_neighbors = n_neighbors
        self.model = LocalOutlierFactor(
            contamination=self.contamination,
            n_neighbors=self.n_neighbors,
            novelty=False,
        )

    def fit_predict(self, df: pd.DataFrame, feature_cols: list[str]) -> pd.DataFrame:
        df = df.copy()
        scores = -self.model.fit_predict(df[feature_cols])
        df["anomaly_lof_raw"] = scores
        df["anomaly_lof_norm"] = (
            df["anomaly_lof_raw"] - df["anomaly_lof_raw"].min()
        ) / (df["anomaly_lof_raw"].max() - df["anomaly_lof_raw"].min() + 1e-9)
        return df
