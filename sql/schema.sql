CREATE TABLE IF NOT EXISTS risk_scores (
    id BIGSERIAL PRIMARY KEY,
    entity_id VARCHAR(255) NOT NULL,
    amount DOUBLE PRECISION,
    tx_count INTEGER,
    anomaly_iforest_norm DOUBLE PRECISION,
    anomaly_lof_norm DOUBLE PRECISION,
    risk_score DOUBLE PRECISION
);
