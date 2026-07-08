# ============================================================
# Identity Echo Interface - Streamlit Application
# ============================================================
# A beginner-friendly Streamlit app that collects a user's
# name and message, validates the inputs, and echoes them
# back with a token-count estimate.
# ============================================================

import streamlit as st  # Import the Streamlit library

# ------------------------------------------------------------
# Page Configuration
# Sets the browser tab title and page icon.
# ------------------------------------------------------------
st.set_page_config(
    page_title="Identity Echo Interface",
    page_icon="📡",
    layout="centered",
)

# ------------------------------------------------------------
# Title & Description
# ------------------------------------------------------------
st.title("📡 Identity Echo Interface")

st.markdown(
    """
    Welcome to the **Identity Echo Interface** — a secure transmission terminal.  
    Enter your name and compose your message below, then hit **Transmit** to send
    it through the system. The interface will validate your input and confirm
    receipt of your transmission.
    """
)

st.divider()  # Visual separator

# ------------------------------------------------------------
# Input Fields
# text_input() renders a single-line text box.
# The first argument is the label shown above the box.
# The placeholder argument shows hint text inside the box.
# ------------------------------------------------------------

# Field 1: Name
user_name = st.text_input(
    label="Name",
    placeholder="e.g. Alex Mercer",
    help="Enter the name that will be associated with your transmission.",
)

# Field 2: Message
user_message = st.text_input(
    label="Message",
    placeholder="Type your message here...",
    help="Enter the message you wish to transmit.",
)

st.divider()  # Visual separator

# ------------------------------------------------------------
# Transmit Button
# st.button() returns True only on the click event.
# All logic below runs ONLY when the button is clicked.
# ------------------------------------------------------------
if st.button("🚀 Transmit", use_container_width=True):

    # --------------------------------------------------------
    # Validation: Check if Name is provided
    # --------------------------------------------------------
    if not user_name:  # True when the name field is empty or whitespace-only
        st.error("Please provide your name.")

    # --------------------------------------------------------
    # Validation: Check if Message is provided
    # --------------------------------------------------------
    elif not user_message:  # True when the message field is empty
        st.warning("Please type a message to transmit.")

    # --------------------------------------------------------
    # Success: Both fields are filled — echo the transmission
    # --------------------------------------------------------
    else:
        # Confirm the transmission to the user
        st.success(
            f"Transmission successful! Greetings, {user_name}. "
            f"We received your message: {user_message}"
        )

        # ----------------------------------------------------
        # Advanced Challenge: Token Count Estimation
        # ----------------------------------------------------

        # Step 1: Count the total number of characters in the message
        char_count = len(user_message)  # len() returns the length of the string

        # Step 2: Estimate the number of tokens
        # A common rule of thumb is that 1 token ≈ 4 characters
        token_count = char_count / 4  # Simple division to estimate tokens

        # Step 3: Display the system diagnostic info
        st.info(
            f"System Check: Your message will consume approximately "
            f"{token_count:.2f} tokens from our context window."
            # :.2f formats the float to 2 decimal places
        )

        # Optional: Show a breakdown in an expander for extra clarity
        with st.expander("📊 Transmission Details"):
            col1, col2, col3 = st.columns(3)
            col1.metric("Sender", user_name)
            col2.metric("Characters", char_count)
            col3.metric("Est. Tokens", f"{token_count:.2f}")
