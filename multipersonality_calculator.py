import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load environment variables from a .env file if one exists.
load_dotenv()

# Create the title shown at the top of the Streamlit page.
st.title("MY CHATBOT")

# Let the user choose the style/personality of the chatbot response.
personality = st.sidebar.selectbox(
    "WHO IS THE PERSONALITY WE ARE TALKING TO TODAY?",
    [
        "a common indian man who is frustrated by indian government",
        "a salman khan fan",
        "a little boy who believes the world is a game that only adults play",
    ],
)
intensity = st.sidebar.slider(
    "HOW INTENSE SHOULD THE PERSONALITY BE?",
    min_value=1,
    max_value=10,
    value = 5,
    step=1,
)
# Read the Gemini API key from the environment.
api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("api_key")
if not api_key:
    # Stop the app if no API key is available.
    st.error("Add your Gemini API key to the GOOGLE_API_KEY or api_key environment variable before running the chatbot.")
    st.stop()

# Create the Gemini client using the API key.
client = genai.Client(api_key=api_key)

# Keep a small conversation history in the session so recent messages can be displayed.
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Get the user's question from the text input box.
user_message = st.text_input("START THE CONVERSATION:")




# Run this block when the user clicks the SEND button.
if st.button("SEND"):
    if user_message:
        # Build the prompt that tells Gemini how to behave and what question to answer.
        prompt = (
            f"You are acting as {personality}. Stay completely in character and respond to the user's message appropriately.\n\n"
            f"User: {user_message}"
            f"Personality (intensity {intensity}):"
        )

        # Show a loading spinner while the model is generating a reply.
        with st.spinner(f"Calling  {personality}..."):
            try:
                # Send the prompt to Gemini and get the response.
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt,
                )
            
            except Exception as exc:
                # Show an error message if the API call fails.
                st.error(f"Failed to get a model response: {exc}")
                st.stop()

        # Display the successful result to the user.
        st.success("Call picked!")
        st.write(response.text)

        st.session_state.chat_history.append({"user": user_message, "bot": response.text})
        st.write("Conversation History:")
        st.write(st.session_state.chat_history)
    else:
        # Warn the user if they tried to send an empty message.
        st.warning("Enter a message!")