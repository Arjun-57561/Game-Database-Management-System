🎮 Game Database Management System
Welcome to the Game Database Management System project! This is a user-friendly application built with Streamlit and MySQL, allowing users to manage, update, and explore a database of video games. The project is designed to help game enthusiasts and developers keep track of game details, including titles, genres, developers, platforms, and pricing.

📋 Table of Contents
Features
Project Structure
Technologies Used
Installation
Usage
Database Schema
Contributing
License
🚀 Features
User-Friendly Interface: Easy navigation through a sleek Streamlit app.
Game Inventory Management: Add, update, view, and delete games in the database.
Real-Time Database Integration: Data is stored and retrieved from a MySQL database.
Interactive Visuals: Explore game data with interactive tables and graphics.
Dynamic Home Page: Engaging homepage with genre selection and fun gaming statistics.
📂 Project Structure
sql
Copy code
Game-Database-Management-System/
├── app.py
├── db_utils.py
├── README.md
├── requirements.txt
├── pages/
│   ├── homepage.py
│   ├── add_game.py
│   ├── update_delete_game.py
│   └── game_inventory.py
├── data/
│   └── sample_games.csv
├── assets/
│   └── logo.png
└── sql/
    └── create_tables.sql
app.py: Main file to run the Streamlit app.
db_utils.py: Database utility functions for CRUD operations.
pages/: Contains different pages of the application.
data/: Folder for sample data or exported files.
assets/: Folder for images or other static assets.
sql/: SQL scripts for creating the database and tables.
🛠️ Technologies Used
Frontend: Streamlit (Python Web Framework)
Backend: MySQL
Programming Language: Python
Libraries:
streamlit
mysql-connector-python
pandas
🖥️ Installation
Follow these steps to set up the project locally:

Prerequisites
Python 3.8 or higher
MySQL Server
Git
1. Clone the Repository
bash
Copy code
git clone https://github.com/your-username/Game-Database-Management-System.git
cd Game-Database-Management-System
2. Install Python Dependencies
bash
Copy code
pip install -r requirements.txt
3. Set Up the MySQL Database
Open MySQL Workbench or use the terminal to run the SQL script located in sql/create_tables.sql to create the database and tables.
sql
Copy code
CREATE DATABASE project;
USE project;
-- Table creation commands from your SQL project
Update the MySQL credentials in db_utils.py:
python
Copy code
conn = sql.connect(
    host='localhost',
    user='root',
    password='your-password',
    database='project'
)
4. Run the Streamlit App
bash
Copy code
streamlit run app.py
The app will be accessible at http://localhost:8501.

🗃️ Database Schema
The project uses a MySQL database with the following schema:

Games: game_id, game_title, developer_id, genre, platform_id, price, release_date
Developers: developer_id, developer_name
Platforms: platform_id, platform_name
Categories: category_id, category_name
Refer to the SQL script in sql/create_tables.sql for detailed table definitions.

🧑‍💻 Usage
Home Page: Welcome screen with an introduction and navigation options.
Add Game: Form to add a new game to the database.
Update/Delete Game: Options to update or delete existing game entries.
Game Inventory: View all games in the database with details in a dynamic table.
🤝 Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch: git checkout -b feature/your-feature-name.
Make your changes and commit: git commit -m 'Add some feature'.
Push to the branch: git push origin feature/your-feature-name.
Submit a pull request.
