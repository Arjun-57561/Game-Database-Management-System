import mysql.connector
from mysql.connector import Error
from faker import Faker
import random

DB_CONFIG = {
    'user': 'root',
    'password': 'Aryanm14!',
    'host': 'localhost',
    'database': 'project',
    'auth_plugin': 'mysql_native_password'
}

def create_connection():
    """ Create a database connection to a MySQL database """
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
    return None

fake = Faker()

# Function to initialize the database
def initialize_database():
    conn = create_connection()
    cursor = conn.cursor()

    # Create Developers table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Developers (
            developer_id INT AUTO_INCREMENT PRIMARY KEY,
            developer_name VARCHAR(100) NOT NULL,
            contact_email VARCHAR(100) NOT NULL
        )
    ''')

    # Create Platforms table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Platforms (
            platform_id INT AUTO_INCREMENT PRIMARY KEY,
            platform_name VARCHAR(50) NOT NULL
        )
    ''')

    # Create Categories table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Categories (
            category_id INT AUTO_INCREMENT PRIMARY KEY,
            category_name VARCHAR(50) NOT NULL
        )
    ''')

    # Create Games table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Games (
            game_id INT AUTO_INCREMENT PRIMARY KEY,
            game_title VARCHAR(100) NOT NULL,
            genre VARCHAR(50) NOT NULL,
            release_date DATE NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            developer_id INT,
            platform_id INT,
            FOREIGN KEY (developer_id) REFERENCES Developers(developer_id),
            FOREIGN KEY (platform_id) REFERENCES Platforms(platform_id)
        )
    ''')

    # Create Customers table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customers (
            customer_id CHAR(36) PRIMARY KEY,  -- UUID format
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            phone_number VARCHAR(15),
            address TEXT NOT NULL
        )
    ''')

    # Create Orders table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Orders (
            order_id INT AUTO_INCREMENT PRIMARY KEY,
            order_date DATE NOT NULL,
            customer_id CHAR(36),
            total_amount DECIMAL(10, 2) NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
        )
    ''')

    # Create Order_Items table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Order_Items (
            order_item_id INT AUTO_INCREMENT PRIMARY KEY,
            order_id INT,
            game_id INT,
            quantity INT NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            FOREIGN KEY (order_id) REFERENCES Orders(order_id),
            FOREIGN KEY (game_id) REFERENCES Games(game_id)
        )
    ''')

    # Create Payment_Methods table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Payment_Methods (
            payment_id INT AUTO_INCREMENT PRIMARY KEY,
            payment_method VARCHAR(50) NOT NULL
        )
    ''')

    # Create Customer_Payments table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customer_Payments (
            payment_id INT,
            order_id INT,
            payment_date DATE NOT NULL,
            FOREIGN KEY (payment_id) REFERENCES Payment_Methods(payment_id),
            FOREIGN KEY (order_id) REFERENCES Orders(order_id)
        )
    ''')

    # Create Sales table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Sales (
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
        )
    ''')

    conn.commit()
    conn.close()

# Initialize and populate the database as needed.
initialize_database()