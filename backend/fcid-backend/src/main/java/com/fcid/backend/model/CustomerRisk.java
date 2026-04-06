package com.fcid.backend.model;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
@Table(name = "customer_risk")
@Getter
@Setter
public class CustomerRisk {

    @Id
    @Column(name = "customer_id")
    private String customerId;

    @Column(name = "risk_score")
    private Double riskScore;
}
