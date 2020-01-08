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

INSERT INTO customer (customer_id,first_name,last_name,street_address,city,state,zip)   VALUES ("1","Jane","Smith","1 South Main","Springfield","OH","43215");  
INSERT INTO customer (customer_id,first_name,last_name,street_address,city,state,zip)   VALUES ("2","John","Smith","1 South Main","Springfield","IL","43215"); 
INSERT INTO customer (customer_id,first_name,last_name,street_address,city,state,zip)   VALUES ("3","Amy","Simpson","11 South Main","Springfield","MO","43215"); 
INSERT INTO customer (customer_id,first_name,last_name,street_address,city,state,zip)   VALUES ("4","Jack","Frank","12 South Main","Springfield","TX","43215"); 

