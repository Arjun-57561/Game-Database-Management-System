create database project;
use project;

CREATE TABLE Platforms (
    platform_id INT AUTO_INCREMENT PRIMARY KEY,
    platform_name VARCHAR(50) NOT NULL
);

CREATE TABLE Developers (
    developer_id INT AUTO_INCREMENT PRIMARY KEY,
    developer_name VARCHAR(100) NOT NULL,
    contact_email VARCHAR(100) NOT NULL
);
show tables;

CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL
);

CREATE TABLE Games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,
    game_title VARCHAR(100) NOT NULL,
    genre VARCHAR(50) NOT NULL,
    release_date DATE NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    developer_id INT,
    platform_id INT,
    FOREIGN KEY (developer_id) REFERENCES Developers(developer_id),
    FOREIGN KEY (platform_id) REFERENCES Platforms(platform_id)
);

CREATE TABLE Customers (
    customer_id CHAR(36) PRIMARY KEY,  -- UUID format
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15),
    address TEXT NOT NULL
);

CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    order_date DATE NOT NULL,
    customer_id CHAR(36),
    total_amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Order_Items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    game_id INT,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (game_id) REFERENCES Games(game_id)
);

CREATE TABLE Game_Categories (
    game_category_id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT,
    category_id INT,
    FOREIGN KEY (game_id) REFERENCES Games(game_id),
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

CREATE TABLE Payment_Methods (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    payment_method VARCHAR(50) NOT NULL
);

CREATE TABLE Customer_Payments (
    payment_id INT,
    order_id INT,
    payment_date DATE NOT NULL,
    FOREIGN KEY (payment_id) REFERENCES Payment_Methods(payment_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);

CREATE TABLE Sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    game_id INT,
    sale_date DATE NOT NULL,
    sale_price DECIMAL(10, 2) NOT NULL,
    discount DECIMAL(5, 2),
    quantity_sold INT NOT NULL,
    total_sale DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (game_id) REFERENCES Games(game_id)
);
show tables;

select * from categories;