import streamlit as st
import random

# Define Growth Mindset Challenges
challenges = [
    "Write down 3 things you learned today.",
    "Try something new and reflect on the experience.",
    "Give yourself positive feedback after completing a task.",
    "Reframe a failure as a learning opportunity.",
    "Spend 5 minutes visualizing yourself achieving a big goal.",
    "Ask for feedback from someone and apply it.",
    "Read an article or book about personal growth.",
    "Teach someone else something new today."
]

# Streamlit UI
st.title("🌱 Growth Mindset Challenge")
st.subheader("Embrace challenges and grow every day!")

if st.button("Get a New Challenge"):
    challenge = random.choice(challenges)
    st.write(f"**Your Challenge:** {challenge}")

st.write("---")
st.write("Developed with ❤️ using Streamlit")
