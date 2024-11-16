# app.py
import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="Game Database Management System", layout="wide")

# --- Dark Mode CSS with Improved Font Sizes ---
st.markdown("""
    <style>
        body {
            background-color: #282828;
            color: #FFFFFF;
            font-size: 16px; /* Base font size */
        }
        .stButton>button {
            background-color: #FF5733;
            color: white;
            border-radius: 5px;
            font-size: 16px; /* Button font size */
        }
        .stTextInput>div>input,
        .stTextArea>div>textarea,
        .stSelectbox>div>select {
            background-color: #444444;
            color: white;
            border: 1px solid #555555;
            font-size: 16px; /* Input field font size */
        }
        .stMarkdown {
            color: white;
            font-size: 16px; /* Markdown text size */
        }
        .stHeader, .stSubheader, .stTitle {
            color: #FF5733;  /* Header color */
            font-size: 24px; /* Header font size */
        }
        .stSidebar {
            background-color: #333333;  /* Sidebar background */
            color: white;  /* Sidebar text color */
            font-size: 16px; /* Sidebar text size */
        }
    </style>
""", unsafe_allow_html=True)

# --- Page Setup ---
home_page = st.Page(page="./pages/homepage.py", title="🏠 Welcome to Game Database Management System", default=True)
about_page = st.Page(page="./pages/about.py", title="👥 About Us - Our Story")
add_game_page = st.Page(page="./pages/add_game.py", title="📝 Add New Game")
update_delete_page = st.Page(page="./pages/update_delete_game.py", title="Update/Delete Game")
game_inventory_page = st.Page(page="./pages/game_inventory.py", title="🎮 Game Inventory")

# --- Navigation ---
pg = st.navigation({
    "Home": [home_page],
    "Add Game": [add_game_page],
    "Update/Delete Game": [update_delete_page],
    "Game Inventory": [game_inventory_page],
    "About": [about_page]
})
pg.run()