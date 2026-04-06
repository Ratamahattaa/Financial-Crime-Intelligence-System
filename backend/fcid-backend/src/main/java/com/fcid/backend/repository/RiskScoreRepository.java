package com.fcid.backend.repository;

import com.fcid.backend.entity.RiskScore;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface RiskScoreRepository extends JpaRepository<RiskScore, Long> {

    List<RiskScore> findTop20ByOrderByRiskScoreDesc();
}
