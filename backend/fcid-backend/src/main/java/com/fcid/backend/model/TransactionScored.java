package com.fcid.backend.model;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
@Table(name = "transactions_scored")
@Getter
@Setter
public class TransactionScored {

    @Id
    @Column(name = "transaction_id")
    private Integer transactionId;

    @Column(name = "customer_id")
    private String customerId;

    private Double amount;
    private String country;
    private String channel;
    private java.time.LocalDateTime timestamp;

    @Column(name = "anomaly_iforest")
    private Integer anomalyIForest;

    @Column(name = "anomaly_lof")
    private Integer anomalyLof;
}
