package com.fcid.backend.repository;

import com.fcid.backend.model.TransactionScored;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface TransactionScoredRepository extends JpaRepository<TransactionScored, Integer> {

    List<TransactionScored> findByAnomalyIForestOrAnomalyLof(Integer anomalyIForest, Integer anomalyLof);
}
