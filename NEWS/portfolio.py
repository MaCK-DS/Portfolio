import streamlit as st

# Set page title
st.set_page_config(page_title="My Portfolio", page_icon="🎯")

# Apply dark theme background color
st.markdown("""
    <style>
    .stApp {
        background-color: #121212;
        color: white;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Add profile picture
# st.sidebar.image(r"C:\Users\mayan\Desktop\NEWS\MAYANK PIC_page-0001 (1).jpg", width=450)

# Header
st.title("Welcome to My Portfolio")

# About Me
st.header("About Me")
st.write("Hello! I'm a data scientist with experience in machine learning, LLM engineering, and Power BI. I'm currently preparing for government exams and exploring blockchain technology. This is my portfolio showcasing my work and skills.")

# Skills
st.header("Skills")
st.write("✅ Data Science")
st.write("✅ Machine Learning")
st.write("✅ Power BI")
st.write("✅ Blockchain")
st.write("✅ LLM & Prompt Engineering")

# Projects
st.header("Projects")
st.write("### Project 1: Data Science Dashboard")
st.write("A Power BI dashboard analyzing sales data and profit")
st.markdown("[🔗  View My Power BI Dashboard on GitHub](https://github.com/MaCK-DS/PowerBiDashboard/tree/main/Power%20bi%20dashboard)", unsafe_allow_html=True)
st.write("### Project 2: Chatbot with LLM")
st.write("A chatbot using OpenAI's API for intelligent responses.")
st.write("### Project 3: Blockchain App")
st.write("A blockchain-based ledger system built with Python.")

# Contact
st.header("Contact")
st.write("📧 Email: your.email@example.com")
st.write("🔗 [LinkedIn](https://linkedin.com/in/yourprofile)")
st.write("💻 [GitHub](https://github.com/yourprofile)")

# Footer
st.write("---")
st.write("Made with ❤️ using Streamlit")
