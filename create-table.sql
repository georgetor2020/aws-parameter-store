USE DevDB;

DROP TABLE IF EXISTS customer;

CREATE TABLE customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) ,
    last_name VARCHAR(255) ,
    street_address VARCHAR(255) ,
    city VARCHAR(255) ,
    state VARCHAR(255) ,
    zip VARCHAR(10)
)  ;
