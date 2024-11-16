import mysql.connector
from database import initialize_database  # Import the initialize_database
DB_CONFIG = {
    'user': 'root',
    'password': 'Aryanm14!',
    'host': 'localhost',
    'database': 'project',
}


def create_connection():
    """ Create a database connection to a MySQL database """

    return mysql.connector.connect(**DB_CONFIG)


def get_all_games():
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Games")

    games = cursor.fetchall()

    cursor.close()
    conn.close()

    return games


def add_game(game_title, developer_id, developer_name, genre, platform_id, platform_name, price, release_date):
    conn = create_connection()
    cursor = conn.cursor()

    # Check if developer_id exists, and insert if it does not
    cursor.execute("SELECT developer_id FROM Developers WHERE developer_id = %s", (developer_id,))
    if not cursor.fetchone():
        print("Developer ID not found. Adding developer to the Developers table.")
        cursor.execute(
            "INSERT INTO Developers (developer_id, developer_name) VALUES (%s, %s)",
            (developer_id, developer_name)
        )

    # Check if platform_id exists, and insert if it does not
    cursor.execute("SELECT platform_id FROM Platforms WHERE platform_id = %s", (platform_id,))
    if not cursor.fetchone():
        print("Platform ID not found. Adding platform to the Platforms table.")
        cursor.execute(
            "INSERT INTO Platforms (platform_id, platform_name) VALUES (%s, %s)",
            (platform_id, platform_name)
        )

    # Proceed with inserting the game
    cursor.execute(
        "INSERT INTO Games (game_title, developer_id, genre, platform_id, price, release_date) VALUES (%s, %s, %s, %s, %s, %s)",
        (game_title, developer_id, genre, platform_id, price, release_date)
    )

    conn.commit()
    cursor.close()
    conn.close()




def update_game(game_id, game_title, developer_id, genre, platform_id, price, release_date):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Games 
        SET game_title=%s, developer_id=%s, genre=%s, platform_id=%s, price=%s, release_date=%s 
        WHERE game_id=%s""",
        (game_title, developer_id, genre, platform_id, price, release_date, game_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_game(game_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Games WHERE game_id=%s", (game_id,))
    conn.commit()
    cursor.close()
    conn.close()


def delete_game(game_id):
    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("DELETE FROM Games WHERE game_id=%s", (game_id,))

    conn.commit()

    cursor.close()
    conn.close()