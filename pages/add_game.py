import streamlit as st
from db_utils import add_game # Ensure this function exists in your db_utils

st.title("Add New Game")

with st.form(key='add_game_form'):
    game_title = st.text_input("Game Title")
    developer_id = st.number_input("Developer ID", min_value=1)
    developer_name = st.text_input("Developer Name")
    genre = st.selectbox("Genre", ['Action', 'Adventure', 'Strategy', 'Puzzle', 'RPG'])
    platform_id = st.number_input("Platform ID", min_value=1)
    platform_name = st.text_input("Platform Name")
    price = st.number_input("Price", min_value=0.0)
    release_date = st.date_input("Release Date")

    submit_button = st.form_submit_button(label='Add Game')

if submit_button:  # Corrected indentation
    add_game(game_title, developer_id, developer_name, genre, platform_id, platform_name, price, release_date)

    st.success("Game added successfully!")