CREATE TABLE IF NOT EXISTS dim_product(
    product_id int primary key,
    product_name varchar(255),
    category varchar(255)
);
CREATE TABLE IF NOT EXISTS dim_customer(
    customer_id int primary key,
    customer_name varchar(255),
    city varchar(255)
);
CREATE TABLE IF NOT EXISTS dim_order(
    order_id int primary key,
    order_date date,
    customer_id int,
    foreign key (customer_id) references dim_customer(customer_id)
);
CREATE TABLE IF NOT EXISTS fact_sales(
    sales_id int primary key,
    order_id int,
    product_id int,
    quantity int,
    price decimal(10,2),
    foreign key (order_id) references dim_order(order_id),
    foreign key (product_id) references dim_product(product_id)
);