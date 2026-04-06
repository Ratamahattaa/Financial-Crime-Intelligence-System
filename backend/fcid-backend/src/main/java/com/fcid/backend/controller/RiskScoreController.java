package com.fcid.backend.controller;

import com.fcid.backend.entity.RiskScore;
import com.fcid.backend.service.RiskScoreService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/risk-scores")
@CrossOrigin(origins = "*")
public class RiskScoreController {

    private final RiskScoreService service;

    public RiskScoreController(RiskScoreService service) {
        this.service = service;
    }

    @GetMapping("/top")
    public List<RiskScore> getTopRiskScores() {
        return service.getTopRiskScores();
    }

    @GetMapping
    public List<RiskScore> getAll() {
        return service.getAll();
    }
}
