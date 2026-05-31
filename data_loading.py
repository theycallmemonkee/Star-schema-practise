import sys
print(sys.executable)
import psycopg2
print("psycopg2 imported successfully")

try:
    conn = psycopg2.connect(
        host="localhost",
        database="starschema",
        user="yogesh",
        password="mehta@07303#")
    cur = conn.cursor()

    cur.execute("""INSERT INTO dim_customer
(customer_id, customer_name, city)
VALUES
(1, 'Yogesh Mehta', 'Delhi'),
(2, 'Rahul Sharma', 'Mumbai'),
(3, 'Amit Verma', 'Bangalore'),
(4, 'Priya Singh', 'Pune'),
(5, 'Neha Gupta', 'Hyderabad'),
(6, 'Arjun Patel', 'Ahmedabad'),
(7, 'Rohit Kumar', 'Chandigarh'),
(8, 'Sneha Jain', 'Jaipur'),
(9, 'Karan Malhotra', 'Kolkata'),
(10, 'Ananya Das', 'Chennai')""")
    conn.commit()

    cur.execute("""INSERT INTO dim_product
(product_id, product_name, category)
VALUES
(1, 'Laptop', 'Electronics'),
(2, 'Mobile', 'Electronics'),
(3, 'Shirt', 'Clothing'),
(4, 'Pant', 'Clothing'),
(5, 'Shoes', 'Footwear')""")
    conn.commit()

    cur.execute("""INSERT INTO dim_order
(order_id, order_date, customer_id)
VALUES
(1, '2024-01-15', 1),
(2, '2024-01-20', 2),
(3, '2024-01-25', 3),
(4, '2024-02-01', 4),
(5, '2024-02-05', 5),
(6, '2024-02-10', 6),
(7, '2024-02-15', 7),
(8, '2024-02-20', 8),
(9, '2024-02-25', 9),
(10, '2024-03-01', 10)""")
    conn.commit()

    cur.execute("""INSERT INTO fact_sales
(sales_id, order_id, product_id, price)
VALUES
(1, 1, 1, 1000.00),
(2, 2, 2, 500.00),
(3, 3, 3, 50.00),
(4, 4, 4, 60.00),
(5, 5, 5, 80.00),
(6, 6, 1, 1000.00),
(7, 7, 2, 500.00),
(8, 8, 3, 50.00),
(9, 9, 4, 60.00),
(10, 10, 5, 80.00)""")
    conn.commit()

    print("Data successfully inserted!")

except Exception as e:
    print(f"Error: {e}")
    conn.rollback()

finally:
    cur.close()
    conn.close()
