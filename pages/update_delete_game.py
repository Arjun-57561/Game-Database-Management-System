import streamlit as st
import pandas as pd
from db_utils import update_game, delete_game, create_connection

# Title for the page
st.title("Update or Delete Game")

# --- Update Game Section ---
st.header("Update Game")
game_id = st.number_input("Game ID to update", min_value=1, step=1)

if game_id:
    conn = create_connection()
    game = pd.read_sql(f"SELECT * FROM Games WHERE game_id = {game_id}", conn)
    conn.close()

    if not game.empty:
        with st.form(key='update_game_form'):
            game_title = st.text_input("Game Title", value=game['game_title'][0])
            developer_id = st.number_input("Developer ID", min_value=1, value=game['developer_id'][0])
            genre = st.selectbox("Genre", ['Action', 'Adventure', 'Strategy', 'Puzzle', 'RPG'],
                                 index=['Action', 'Adventure', 'Strategy', 'Puzzle', 'RPG'].index(game['genre'][0]))
            platform_id = st.number_input("Platform ID", min_value=1, value=game['platform_id'][0])
            price = st.number_input("Price", min_value=0.0, value=game['price'][0])
            release_date = st.date_input("Release Date", value=pd.to_datetime(game['release_date'][0]))

            submit_button = st.form_submit_button(label='Update Game')

            if submit_button:
                update_game(game_id, game_title, developer_id, genre, platform_id, price, release_date)
                st.success("Game updated successfully!")
    else:
        st.warning("Game not found.")

# --- Delete Game Section ---
st.header("Delete Game")
delete_game_id = st.number_input("Game ID to delete", min_value=1, step=1)

if delete_game_id:
    if st.button("Delete Game"):
        delete_game(delete_game_id)
        st.success("Game deleted successfully!")
