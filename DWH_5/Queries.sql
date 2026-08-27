-- 1. Продажи по месяцам (сколько заработали в каждом месяце)
SELECT d.year, d.month, SUM(f.total) AS total_sales
FROM fact_sales f
JOIN dim_date d ON f.date_sk = d.date_sk
GROUP BY d.year, d.month
ORDER BY d.year, d.month;

-- 2. Топ-5 товаров по выручке (какие товары приносят больше всего денег)
SELECT p.product_name, SUM(f.total) AS total_revenue
FROM fact_sales f
JOIN dim_product p ON f.product_sk = p.product_sk
GROUP BY p.product_name
ORDER BY total_revenue DESC
LIMIT 5;

-- 3. Продажи по городам (из каких городов приходит больше всего заказов)
SELECT c.city, SUM(f.total) AS total_sales
FROM fact_sales f
JOIN dim_customer c ON f.customer_sk = c.customer_sk
GROUP BY c.city
ORDER BY total_sales DESC;