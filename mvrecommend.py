import streamlit as st
import google.generativeai as genai

# 🔐 Gemini API Key only
GEMINI_API_KEY = "AIzaSyBF5zbsSYPsMw--JIdE8FKEtgytg9ftHF4"

# 🌟 Configure Gemini
genai.configure(api_key="AIzaSyBF5zbsSYPsMw--JIdE8FKEtgytg9ftHF4")
model = genai.GenerativeModel("gemini-2.0-flash")

# 🤖 Use Gemini to generate movie recommendations
def recommend_movies(genre, actor, plot):
    prompt = f"""
You are a smart movie friend. Recommend 5 movies based on these preferences:
- Genre: {genre}
- Favorite Actor: {actor if actor else 'Any'}
- Plot Type: {plot}

For each movie, provide:
1. Title
2. Reason why it matches the user's taste
3. 1-2 sentence plot summary

Format as:
Title: ...
Reason: ...
Plot: ...
---
"""
    response = model.generate_content(prompt)
    return response.text

# 📱 Streamlit App UI
st.set_page_config(page_title="🎥 Gemini Movie Buddy", layout="centered")
st.title("🎬 Gemini Movie Buddy")
st.markdown("Let’s find your perfect movie match! 🍿")

genre = st.text_input("🎭 Favorite genre? (e.g., Action, Drama, Romance)")
actor = st.text_input("🌟 Favorite actor? (Optional)")
plot = st.text_input("📚 What kind of plot do you enjoy? (e.g., time travel, love triangle, revenge)")

if st.button("🎯 Recommend Me Movies"):
    if not genre or not plot:
        st.warning("Please provide at least a genre and plot preference.")
    else:
        with st.spinner("Finding your next favorite movie..."):
            result_text = recommend_movies(genre, actor, plot)

        # Split results by movie
        movies = [block.strip() for block in result_text.split('---') if block.strip()]
        
        st.subheader("🎁 Your Personalized Picks:")
        for movie in movies:
            lines = movie.split("\n")
            title = next((line.split("Title:")[1].strip() for line in lines if "Title:" in line), "Unknown")
            reason = next((line.split("Reason:")[1].strip() for line in lines if "Reason:" in line), "")
            plot_summary = next((line.split("Plot:")[1].strip() for line in lines if "Plot:" in line), "")

            st.markdown(f"### 🎥 {title}")
            st.image("https://via.placeholder.com/300x450.png?text=No+Poster", width=200)  # Static fallback image
            st.markdown(f"**Why you'll love it**: {reason}")
            st.markdown(f"📝 **Plot Summary**: {plot_summary}")
            st.markdown("---")
