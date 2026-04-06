package com.fcid.backend.service;

import com.fcid.backend.model.CustomerRisk;
import com.fcid.backend.model.TransactionScored;
import com.fcid.backend.repository.CustomerRiskRepository;
import com.fcid.backend.repository.TransactionScoredRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class AnalyticsService {

    private final TransactionScoredRepository txRepo;
    private final CustomerRiskRepository riskRepo;

    public AnalyticsService(TransactionScoredRepository txRepo, CustomerRiskRepository riskRepo) {
        this.txRepo = txRepo;
        this.riskRepo = riskRepo;
    }

    public List<TransactionScored> getAnomalies() {
        return txRepo.findByAnomalyIForestOrAnomalyLof(1, 1);
    }

    public List<CustomerRisk> getTopRiskCustomers() {
        return riskRepo.findAll()
                .stream()
                .sorted((a, b) -> Double.compare(b.getRiskScore(), a.getRiskScore()))
                .limit(20)
                .toList();
    }
}
