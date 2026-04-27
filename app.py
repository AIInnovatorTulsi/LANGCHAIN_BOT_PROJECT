import streamlit as st
from router import route
from phase3 import generate_defense_reply

st.set_page_config(page_title="AI Bot System")

st.title("🤖 AI Bot System")

# User input
user_input = st.text_area("Enter your post:")

if st.button("Generate Response"):

    if user_input.strip() == "":
        st.warning("Please enter some text")
    else:
        # Step 1: Find best bot
        bots = route(user_input)
        selected_bot = bots[0] if bots else "BotA"

        # Step 2: Define persona
        bot_persona = """
        I believe AI and technology are the future.
        I strongly support innovation.
        """

        # Step 3: Generate reply
        reply = generate_defense_reply(
            bot_persona,
            user_input,
            "",
            "User comment"
        )

        # Output
        st.success(f"Selected Bot: {selected_bot}")
        st.write("### 🤖 Reply:")
        st.write(reply)