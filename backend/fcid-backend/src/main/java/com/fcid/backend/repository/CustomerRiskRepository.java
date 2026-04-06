package com.fcid.backend.repository;

import com.fcid.backend.model.CustomerRisk;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CustomerRiskRepository extends JpaRepository<CustomerRisk, String> {
}
