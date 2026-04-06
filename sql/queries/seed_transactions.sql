INSERT INTO customers (customer_id, country, segment) VALUES
('1001', 'PL', 'retail'),
('1002', 'DE', 'retail'),
('1003', 'UA', 'corporate'),
('1004', 'PL', 'retail');

INSERT INTO transactions (customer_id, sender, receiver, amount, country, channel, timestamp) VALUES
('1001', 'A001', 'B001', 5000, 'PL', 'online', NOW() - INTERVAL '2 days'),
('1002', 'A002', 'B003', 120000, 'CY', 'branch', NOW() - INTERVAL '1 day'),
('1001', 'A003', 'B002', 300, 'PL', 'online', NOW() - INTERVAL '3 hours'),
('1003', 'A004', 'B004', 75000, 'UA', 'online', NOW() - INTERVAL '5 hours'),
('1004', 'A005', 'B006', 200, 'PL', 'atm', NOW() - INTERVAL '1 hour');
