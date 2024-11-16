import streamlit as st

# Initialize session state
if "Name" not in st.session_state:
    st.session_state["Name"] = ""
if "Login" not in st.session_state:
    st.session_state["Login"] = ""
if "Id" not in st.session_state:
    st.session_state["Id"] = ""

# Set a title for your site
st.title("🎮 Game Store Inventory Manager")

# Inspirational Story Section
st.markdown(
    """
    <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);'>
        <h4 style='color: #ff5733;'>Our Inspiring Journey</h4>
        <ul style='color: #555;'>
            <li>In a bustling tech hub, three passionate engineers—Bontha Mallikarjun Reddy, Aryan Mallick, and Aakash Sharma—shared a common dream: to revolutionize the way game stores operate.</li>
            <li>As dedicated gamers themselves, they often found themselves wandering through local game stores. Each visit revealed the same struggle: store owners wrestling with outdated systems and cumbersome manual processes that hindered their ability to serve customers effectively.</li>
            <li>Fueled by their love for gaming and a desire to empower these businesses, they united their skills and embarked on an ambitious journey. They envisioned a comprehensive platform that would streamline inventory management, allowing store owners to focus on what truly mattered—delivering exceptional gaming experiences.</li>
            <li>Through countless brainstorming sessions, late-night coding marathons, and rigorous testing phases, the trio brought their vision to life. They launched the Game Store Inventory Management System, packed with features like real-time sales tracking and intuitive order processing—all designed with the user in mind.</li>
            <li>Today, Bontha, Aryan, and Aakash stand proud as they witness their creation making waves in the gaming community. Their commitment to continuous innovation ensures that the platform evolves alongside the needs of game stores everywhere.</li>
            <li>Join us on this exciting journey as we empower game store owners to manage their businesses efficiently and effectively!</li>
        </ul>
    </div>
    """, unsafe_allow_html=True
)

# LinkedIn Profiles Section
st.markdown(
    """
    <div style='text-align: center; margin-top: 20px;'>
        <h4 style='color: #ff5733;'>Connect with Us on LinkedIn</h4>
        <p>Follow our team for updates and insights:</p>
        <a href="https://www.linkedin.com/in/aryan-mallick-0b16692a1/" target="_blank" style="color: #ff5733;">Aryan Mallick</a> | 
        <a href="https://www.linkedin.com/in/mallikarjun-reddy-574a53287/" target="_blank" style="color: #ff5733;">Bontha Mallikarjun Reddy</a> | 
        <a href="https://www.linkedin.com/in/aakash-sharma-a33903278/" target="_blank" style="color: #ff5733;">Aakash Sharma</a>
    </div>
    """, unsafe_allow_html=True
)

# Engineers' Photos Section using st.image()
st.markdown(
    """
    <div style='text-align: center; margin-top: 40px;'>
        <h4 style='color: #ff5733;'>Meet Our Team</h4>
    </div>
    """, unsafe_allow_html=True
)

# Display engineers' photos with st.image()
col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/aryan.jpg", caption="Aryan Mallick", width=250)

with col2:
    st.image("images/ash.jpg", caption="Bontha Mallikarjun Reddy", width=250)

with col3:
    st.image("images/Aakash.jpg", caption="Aakash Sharma", width=250)

# Optional Footer
st.markdown(
    """
    <div style='text-align: center; margin-top: 20px;'>
        <p style='color: #555;'>Game Database Management System © 2024</p>
    </div>
    """, unsafe_allow_html=True
)