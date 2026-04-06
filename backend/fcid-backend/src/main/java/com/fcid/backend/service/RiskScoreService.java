package com.fcid.backend.service;

import com.fcid.backend.entity.RiskScore;
import com.fcid.backend.repository.RiskScoreRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class RiskScoreService {

    private final RiskScoreRepository repository;

    public RiskScoreService(RiskScoreRepository repository) {
        this.repository = repository;
    }

    public List<RiskScore> getTopRiskScores() {
        return repository.findTop20ByOrderByRiskScoreDesc();
    }

    public List<RiskScore> getAll() {
        return repository.findAll();
    }
}
