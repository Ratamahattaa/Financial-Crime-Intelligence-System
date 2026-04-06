CREATE TABLE customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    country VARCHAR(50),
    segment VARCHAR(50)
);

CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    customer_id VARCHAR(20) REFERENCES customers(customer_id),
    sender VARCHAR(50),
    receiver VARCHAR(50),
    amount NUMERIC(12,2),
    country VARCHAR(50),
    channel VARCHAR(50),
    timestamp TIMESTAMP
);

CREATE TABLE transactions_scored (
    transaction_id INT PRIMARY KEY,
    customer_id VARCHAR(20),
    amount NUMERIC(12,2),
    country VARCHAR(50),
    channel VARCHAR(50),
    timestamp TIMESTAMP,
    anomaly_iforest INT,
    anomaly_lof INT
);

CREATE TABLE customer_risk (
    customer_id VARCHAR(20) PRIMARY KEY,
    risk_score NUMERIC(5,4)
);
