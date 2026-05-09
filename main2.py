import streamlit as st #for input from webpage
from google import genai
import os

st.title("AI Business Validator")
#st.header("This is my personnel GPT")

key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=key)

audience = st.text_input("Who are your audience? ")
age_group = st.text_input("Which is your age group? ")
country = st.text_input("Which country are you targeting? ")
idea = st.text_input("Give your business idea: ")

prompt = f"""
Generate a detailed startup concept based on the following information:
Audience: {audience}
Age Group: {age_group}
Target Country: {country}
Business Idea: {idea}
Requirements:
1. Describe the business model clearly.
2. Explain the problem it solves and how it’s unique in {country}.
3. Identify potential competitors and differentiation strategies.
4. Suggest a marketing approach tailored to {age_group} in {country}.
5. Include potential revenue streams and startup cost considerations.
6. End with a short elevator pitch (under 50 words)
"""
if st.button("Generate Report"):
    with st.spinner("Generating Report.."):
        response = client.models.generate_content(
                model = "gemini-2.5-flash",
                contents = prompt
                )
        st.write(response.text)
