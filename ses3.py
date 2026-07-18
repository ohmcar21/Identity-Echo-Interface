import streamlit as st 

st.title("MY CHATBOT")

personality = st.sidebar.selectbox("WHO IS THE PERSONALITY WE ARE TALKING TO TODAY?",[
    "donald trump" , "a poor man who has a bad ego" ,"a common indian man who is frustrated by indian goverment", " a crazy salman khan fan" , "a little boy who beleives the world is a game that only adults play"
])

from google import genai
import os 
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("api_key"))
user_message = st.text_input("START THE CONVERSATION:")


if st.button("SEND"):
    if user_message :
        ai_inst = {f"You are acting as {personality} and stay completely in character and respond in tone necessary to the question asked.",
                   f"User message = {user_message}
        with st.spinner(f"calling a {personality}"):  #animaton
            response = client.models._generate_content(
                model = "gemini-2.5-flash",
                contents = ai_inst,
            ) # gemeni takes the unput and climbs the bridge 
            st.success("call picked!")
            st.write(response.text)
    else :
        st.warning("enter a message!")