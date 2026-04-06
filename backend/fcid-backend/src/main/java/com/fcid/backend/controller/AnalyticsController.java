package com.fcid.backend.controller;

import com.fcid.backend.model.CustomerRisk;
import com.fcid.backend.model.TransactionScored;
import com.fcid.backend.service.AnalyticsService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*")
public class AnalyticsController {

    private final AnalyticsService service;

    public AnalyticsController(AnalyticsService service) {
        this.service = service;
    }

    @GetMapping("/anomalies")
    public List<TransactionScored> getAnomalies() {
        return service.getAnomalies();
    }

    @GetMapping("/risk/customers")
    public List<CustomerRisk> getTopRiskCustomers() {
        return service.getTopRiskCustomers();
    }
}
