import streamlit as st

# Initialize session state
if "Name" not in st.session_state:
    st.session_state["Name"] = ""
if "Login" not in st.session_state:
    st.session_state["Login"] = ""
if "Id" not in st.session_state:
    st.session_state["Id"] = ""

# Set a title for your site
st.title("🎮 Game Store & Database Management System")

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

# Introduction Section
st.markdown(
    """
    <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);'>
        <h5 style='color: #333;'>Welcome to the Game Store Inventory Manager!</h5>
        <p style='color: #555;'>Manage your video game stock, sales, and customer orders with ease. 
        Our platform simplifies your inventory management and enhances your ability to provide top-notch service.</p>
    </div>
    """, unsafe_allow_html=True
)

# Image Section
col1, col2 = st.columns([1, 3])
with col1:
    st.image("images/mon.webp", use_container_width=True)  # Use responsive width

with col2:
    st.header("Explore Your Favorite Games!")

st.write("---")

# Features Section
st.header("Why Choose Us?")
features = [
    "🎯 Streamlined Inventory Management",
    "📊 Real-Time Sales Tracking",
    "📦 Customer Order Management",
    "🖥️ Easy-to-Use Interface",
    "📈 Data-Driven Insights for Business Growth"
]

for feature in features:
    st.markdown(f"- {feature}")

st.write("---")

# Competitive Analysis Section
st.header("Why We're the Best")
col3, col4 = st.columns(2)
with col3:
    st.image("images/3.jpg", use_container_width=True)  # Use responsive width

with col4:
    st.write(
        "Our platform stands out due to its unique features and user-centric design. Here's how we compare:"
    )

    competitors = {
        "Competitor A": {
            "Pros": "Established brand with a loyal user base.",
            "Cons": "Clunky interface and limited features."
        },
        "Competitor B": {
            "Pros": "Mobile accessibility and ease of use.",
            "Cons": "Lacks comprehensive inventory tools."
        },
        "Game Store Inventory Manager": {
            "Pros": "All-in-one solution with real-time tracking.",
            "Cons": "None! We're continuously innovating."
        }
    }

    for name, details in competitors.items():
        st.subheader(name)
        st.write(f"**Pros:** {details['Pros']}")
        st.write(f"**Cons:** {details['Cons']}")

st.write("---")

# Key Features Section
st.header("Key Features of Our Platform")
features_list = [
    ("Comprehensive Inventory Management", "#FFDDC1"),  # Light peach
    ("Real-Time Sales Tracking", "#D1FAE5"),              # Light green
    ("Customer Relationship Management", "#CFFAFE"),     # Light blue
    ("User-Friendly Interface", "#FEF9C3")                # Light yellow
]

for feature, color in features_list:
    st.markdown(
        f"""
        <div style='background-color: {color}; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
            <h5 style='color: #333;'>{feature}</h5>
        </div>
        """, unsafe_allow_html=True
    )

# Game Exploration Section
st.markdown("<h3 style='color: #ff5733;'>Manage, Update, and Explore Your Favorite Games!</h3>", unsafe_allow_html=True)

# Interactive Game Genre Selector
genre = st.selectbox("What type of game are you looking for?", ['Action', 'Adventure', 'RPG', 'Strategy', 'Puzzle'])

games = {
    'Action': ['Doom Eternal', 'Sekiro', 'Hades'],
    'Adventure': ['The Legend of Zelda: Breath of the Wild', 'Firewatch', 'Journey'],
    'RPG': ['The Witcher 3', 'Persona 5', 'Final Fantasy VII Remake'],
    'Strategy': ['Civilization VI', 'XCOM 2', 'StarCraft II'],
    'Puzzle': ['Portal 2', 'The Witness', 'Tetris Effect']
}

if genre in games:
    st.markdown(f"### Recommended {genre} Games:")
    for game in games[genre]:
        st.write(f"- {game}")

# Fun Facts Section
st.markdown("### Did you know?")
st.write("""
- **Over 2.7 billion gamers** worldwide in 2024.
- The **most expensive video game ever made** was *Grand Theft Auto V*, costing over $270 million.
- **Mobile gaming** is expected to generate more than **$100 billion** in revenue this year.
""")

# User Poll or Feedback Section
favorite_genre = st.radio("What's your favorite game genre?", ['Action', 'Adventure', 'RPG', 'Strategy', 'Puzzle'])

if st.button("Vote"):
    st.write(f"Thank you for voting for **{favorite_genre}**!")

# Game Trivia Quiz
st.markdown("### Test Your Knowledge!")
quiz_answer = st.selectbox("What year was the first video game released?", [1971, 1980, 1985, 1990])

if st.button("Submit Answer"):
    if quiz_answer == 1971:
        st.success("Correct! The first video game was released in 1971.")
    else:
        st.error("Incorrect! The correct answer is 1971.")

# Carousel-like Feature for Games Images
st.header("Featured Games")
col5, col6, col7 = st.columns(3)

with col5:
    st.image("images/minecraft.jpg", caption="Minecraft", use_container_width=True)

with col6:
    st.image("images/eldenring.jpg", caption="Elden Ring", use_container_width=True)

with col7:
    st.image("images/valorant.jpg", caption="Valorant", use_container_width=True)

# Call to Action Section
st.markdown(
    """
    <div style='text-align: center; margin-top: 20px;'>
        <h4 style='color: #ff5733;'>Join us today!</h4>
        <p>Experience how Game Store Inventory Manager can transform your business.</p>
        <a href="#" style='background-color: #ff5733; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none;'>Get Started</a>
    </div>
    """, unsafe_allow_html=True
)

# Footer with Social Media Links
st.markdown("""
<div style='background-color: #333; color: white; padding: 10px; text-align: center; margin-top: 20px; border-radius: 10px;'>
   <p>Game Database Management System © 2024</p>
   <p>Follow us on LinkedIn:</p>
   <a href="https://www.linkedin.com/in/mallikarjun-reddy-574a53287/" target="_blank" style="color: white;">Bontha Mallikarjun Reddy</a> |
   <a href="https://www.linkedin.com/in/aryan-mallick-0b16692a1/" target="_blank" style="color: white;">Aryan Mallick</a> |
   <a href="https://www.linkedin.com/in/aakash-sharma-a33903278/" target="_blank" style="color: white;">Aakash Sharma</a>
</div>
""", unsafe_allow_html=True)