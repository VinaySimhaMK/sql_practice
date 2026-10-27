import sqlite3
import pandas as pd

conn = sqlite3.connect("practice.db")
conn.executescript("""
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS orders;

CREATE TABLE customers (customer_id INTEGER, name TEXT, city TEXT);
INSERT INTO customers VALUES
(1, 'Arun', 'Chennai'),
(2, 'Priya', 'Bangalore'),
(3, 'Karthik', 'Hyderabad'),
(4, 'Meena', 'Chennai'),
(5, 'Ravi', 'Bangalore');

CREATE TABLE orders (order_id INTEGER, customer_id INTEGER, item TEXT, amount INTEGER, order_date TEXT);
INSERT INTO orders VALUES
(101, 1, 'pen', 10, '2026-10-01'),
(102, 2, 'book', 50, '2026-10-02'),
(103, 1, 'bag', 200, '2026-10-03'),
(104, 3, 'bottle', 120, '2026-10-04'),
(105, 4, 'notebook', 40, '2026-10-05'),
(106, 2, 'bag', 200, '2026-10-06'),
(107, 4, 'pen', 10, '2026-10-07'),
(108, 1, 'book', 50, '2026-10-08');
""")

queries = {
    "Task 1: orders above 40, newest first": """
        SELECT * FROM orders
        WHERE amount > 40
        ORDER BY order_date DESC
    """,
    "Task 2: total spent per customer, including customers with no orders": """
        SELECT c.name, SUM(o.amount) AS total
        FROM customers c
        LEFT JOIN orders o ON c.customer_id = o.customer_id
        GROUP BY c.name
        ORDER BY total DESC
    """,
    "Task 3: cities with total above 200 (HAVING)": """
        SELECT c.city, SUM(o.amount) AS total
        FROM customers c
        LEFT JOIN orders o ON c.customer_id = o.customer_id
        GROUP BY c.city
        HAVING SUM(o.amount) > 200
        ORDER BY SUM(o.amount) DESC
    """,
    "Task 4: orders above the average amount (subquery)": """
        SELECT * FROM orders
        WHERE amount > (SELECT AVG(amount) FROM orders)
    """,
    "Task 5: ranking all orders by amount (RANK)": """
        SELECT order_id, item, amount,
               RANK() OVER (ORDER BY amount DESC) AS amount_rank
        FROM orders
    """,
    "Task 5b: same with DENSE_RANK": """
        SELECT order_id, item, amount,
               DENSE_RANK() OVER (ORDER BY amount DESC) AS amount_rank
        FROM orders
    """,
    "Task 6: rank within each customer (PARTITION BY)": """
        SELECT customer_id, order_id, amount,
               RANK() OVER (PARTITION BY customer_id ORDER BY amount DESC) AS order_rank
        FROM orders
    """,
    "Task 7: each customer's biggest order": """
        SELECT customer_id, order_id, amount
        FROM (
            SELECT customer_id, order_id, amount,
                   RANK() OVER (PARTITION BY customer_id ORDER BY amount DESC) AS order_rank
            FROM orders
        ) AS ranked
        WHERE order_rank = 1
    """,
}

for title, query in queries.items():
    print(title)
    print(pd.read_sql(query, conn))
    print()

conn.close()