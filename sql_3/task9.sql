SELECT
    o.order_id,
    c.customer_id,
    o.item,
    o.amount,
    SUM(o.amount) OVER (PARTITION BY c.customer_id) AS total_by_customer
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id;