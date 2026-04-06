package com.fcid.backend.entity;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "risk_scores")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class RiskScore {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "entity_id", nullable = false)
    private String entityId;

    @Column(name = "amount")
    private Double amount;

    @Column(name = "tx_count")
    private Integer txCount;

    @Column(name = "anomaly_iforest_norm")
    private Double anomalyIForestNorm;

    @Column(name = "anomaly_lof_norm")
    private Double anomalyLofNorm;

    @Column(name = "risk_score")
    private Double riskScore;
}
