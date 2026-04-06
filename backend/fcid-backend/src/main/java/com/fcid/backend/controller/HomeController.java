package com.fcid.backend.controller;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping({"/", "/error"})
@CrossOrigin(origins = "*")
public class HomeController {

    @GetMapping
    public String home() {
        return "Financial Crime Intelligence backend is running. Available endpoints: /api/risk-scores, /api/risk-scores/top, /api/anomalies, /api/risk/customers";
    }
}
