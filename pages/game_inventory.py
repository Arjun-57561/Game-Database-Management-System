import streamlit as st
from db_utils import get_all_games
import pandas as pd


def show_game_inventory_page():
    st.title("🎮 Game Inventory")

    # Add a brief introduction with styled markdown
    st.markdown("""
        <div style='background-color: #f0f8ff; padding: 20px; border-radius: 10px;'>
            <h2 style='color: #333;'>Welcome to the Game Inventory</h2>
            <p style='color: #555;'>Here you can find all the games available in our inventory. 
            Browse through our collection to manage your stock effectively.</p>
        </div>
    """, unsafe_allow_html=True)

    # Fetch the games data
    games_data = get_all_games()

    if isinstance(games_data, pd.DataFrame) and not games_data.empty:  # Check if it's a DataFrame
        # Display the games in a table format
        st.markdown("<h3 style='color: #333;'>Current Inventory:</h3>", unsafe_allow_html=True)

        # Use st.dataframe for an interactive table or st.table for a static table
        st.dataframe(games_data.style.highlight_max(axis=0))  # Highlight maximum values in each column

        # Add a section for additional information or tips
        st.markdown("""
            <div style='background-color: #e6ffe6; padding: 15px; border-radius: 10px; margin-top: 20px;'>
                <h3 style='color: #333;'>Tips for Managing Your Inventory:</h3>
                <ul style='color: #555;'>
                    <li>Regularly update your inventory to reflect new arrivals and sales.</li>
                    <li>Use filters to quickly find specific games by genre, platform, or availability.</li>
                    <li>Keep track of customer preferences to enhance your stock decisions.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    elif isinstance(games_data, list) and len(games_data) > 0:  # Check if it's a non-empty list
        st.write("Here are the games in your inventory:")
        for game in games_data:
            st.write(f"- {game}")  # Display each game in the list

    else:
        st.write("🚫 No games found in the inventory.")

# Run the game inventory page function
show_game_inventory_page()