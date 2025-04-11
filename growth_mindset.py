import streamlit as st # type: ignore
import random
import os

# App title and description
st.title("Growth Mindset Challenge 🌱")
st.write("""
Welcome to the Growth Mindset Challenge! A growth mindset is about believing you can grow through effort, learning, and persistence.
This app offers daily challenges, quotes, and a space to reflect on your journey.
""")

# Daily Challenges
st.header("Daily Challenge")
challenges = [
    "Learn one new skill today (e.g., a new word, a coding trick, or a fun fact).",
    "Try something you’ve failed at before and reflect on what you learned.",
    "Ask someone for feedback on a project or task and act on it.",
    "Spend 10 minutes reading about a topic you’re curious about.",
    "Write down one thing you’re grateful for and why."
]
if st.button("Get Today’s Challenge"):
    daily_challenge = random.choice(challenges)
    st.success(daily_challenge)

# Inspirational Quotes
st.header("Inspirational Quote")
quotes = [
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "You are never too old to set another goal or to dream a new dream. – C.S. Lewis",
    "Mistakes are the portals of discovery. – James Joyce",
    "Success is not the absence of obstacles, but the courage to push through them. – Unknown",
    "The mind is everything. What you think, you become. – Buddha"
]
if st.button("Show Me a Quote"):
    daily_quote = random.choice(quotes)
    st.info(daily_quote)

# Reflection Journal
st.header("Reflection Journal")
st.write("Reflect on your day or the challenge. What did you learn? How did you grow?")
reflection = st.text_area("Your thoughts...", height=150)

if st.button("Save Reflection"):
    if reflection.strip():
        # Save reflection to a file with a timestamp
        with open("reflections.txt", "a") as f:
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {reflection}\n\n")
        st.success("Reflection saved!")
    else:
        st.error("Please write something before saving.")

# Optional: Display past reflections
if os.path.exists("reflections.txt"):
    if st.checkbox("Show Past Reflections"):
        with open("reflections.txt", "r") as f:
            past_reflections = f.read()
        st.text_area("Your Past Reflections", past_reflections, height=200, disabled=True)

# Footer
st.markdown("---")
st.write("Built with ❤️ using Streamlit. Keep growing!")