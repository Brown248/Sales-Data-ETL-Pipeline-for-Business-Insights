-- 1. ยอดขายรวมทั้งหมด
SELECT SUM(sales) AS total_sales,
       SUM(profit) AS total_profit
FROM sales;

-- 2. ยอดขายรวมแต่ละ Category
SELECT category,
       SUM(sales) AS total_sales,
       SUM(profit) AS total_profit
FROM sales
GROUP BY category
ORDER BY total_sales DESC;

-- 3. Top 5 Sub-Category กำไรสูงสุด
SELECT sub_category,
       SUM(profit) AS total_profit
FROM sales
GROUP BY sub_category
ORDER BY total_profit DESC
LIMIT 5;

-- 4. ยอดขายแต่ละ Region
SELECT region,
       SUM(sales) AS total_sales,
       SUM(profit) AS total_profit
FROM sales
GROUP BY region
ORDER BY total_sales DESC;

-- 5. ข้อมูล summary ของ Discount
SELECT AVG(discount) AS avg_discount,
       MIN(discount) AS min_discount,
       MAX(discount) AS max_discount
FROM sales;

-- 6. จำนวน order แต่ละ Segment
SELECT segment,
       COUNT(*) AS order_count,
       SUM(sales) AS total_sales,
       SUM(profit) AS total_profit
FROM sales
GROUP BY segment
ORDER BY total_sales DESC;
