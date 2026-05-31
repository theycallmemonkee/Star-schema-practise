import sys
print(sys.executable)
import psycopg2
print("psycopg2 imported successfully")
try:
    conn = psycopg2.connect(
        host="localhost",
        database="starschema",
        user="yogesh",
        password="mehta@07303#"
    )

    cur = conn.cursor()

    cur.execute("""
    INSERT INTO dim_customer1
    (customer_id, customer_name, city)
    VALUES
    (1, 'Yogesh', 'Delhi'),
    (2, 'Rahul', 'Mumbai'),
    (3, 'Amit', 'Bangalore'),
    (4, 'Priya', 'Pune'),
    (5, 'Sneha', 'Hyderabad'),
    (6, 'Arjun', 'Chennai'),
    (7, 'Neha', 'Kolkata'),
    (8, 'Rohit', 'Jaipur'),
    (9, 'Ankit', 'Ahmedabad'),
    (10, 'Pooja', 'Lucknow');
    """)

    cur.execute("""
    INSERT INTO dim_order1
    (order_id, order_date, customer_id)
    VALUES
    (101, '2026-05-01', 1),
    (102, '2026-05-02', 2),
    (103, '2026-05-03', 3),
    (104, '2026-05-04', 4),
    (105, '2026-05-05', 5),
    (106, '2026-05-06', 6),
    (107, '2026-05-07', 7),
    (108, '2026-05-08', 8),
    (109, '2026-05-09', 9),
    (110, '2026-05-10', 10);
    """)

    cur.execute("""
    INSERT INTO dim_product1
    (product_id, product_name, category, order_id)
    VALUES
    (1001, 'Laptop', 'Electronics', 101),
    (1002, 'Mouse', 'Electronics', 102),
    (1003, 'Keyboard', 'Electronics', 103),
    (1004, 'Monitor', 'Electronics', 104),
    (1005, 'Headphones', 'Electronics', 105),
    (1006, 'Tablet', 'Electronics', 106),
    (1007, 'Smartphone', 'Electronics', 107),
    (1008, 'Printer', 'Electronics', 108),
    (1009, 'Webcam', 'Electronics', 109),
    (1010, 'Speaker', 'Electronics', 110);
    """)

    cur.execute("""
    INSERT INTO fact_sales1
    (sales_id, order_id, product_id, quantity, price)
    VALUES
    (1, 101, 1001, 1, 50000.00),
    (2, 102, 1002, 2, 1000.00),
    (3, 103, 1003, 1, 2500.00),
    (4, 104, 1004, 1, 15000.00),
    (5, 105, 1005, 2, 3000.00),
    (6, 106, 1006, 1, 25000.00),
    (7, 107, 1007, 1, 40000.00),
    (8, 108, 1008, 1, 8000.00),
    (9, 109, 1009, 2, 2000.00),
    (10, 110, 1010, 3, 1500.00);
    """)

    conn.commit()

    cur.execute("""
    SELECT
        c.customer_name,
        c.city,
        p.product_name,
        o.order_date,
        f.quantity,
        f.price
    FROM fact_sales1 f
    JOIN dim_order1 o
        ON f.order_id = o.order_id
    JOIN dim_customer1 c
        ON o.customer_id = c.customer_id
    JOIN dim_product1 p
        ON f.product_id = p.product_id;
    """)

    rows = cur.fetchall()

    print("\nSales Data:")
    for row in rows:
        print(row)

    print("\nData added successfully")

except Exception as e:
    print("Failed")
    print(e)

    if 'conn' in locals():
        conn.rollback()

finally:
    if 'cur' in locals():
        cur.close()

    if 'conn' in locals():
        conn.close()