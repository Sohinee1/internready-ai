import streamlit as st
from google import genai

st.set_page_config(
    page_title="AI Mentor Chat",
    page_icon="💬",
    layout="wide"
)

st.title("AI Mentor Chat")
st.write("Ask anything about your internship prep, projects, or career doubts.")

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
system_context = """
You are a friendly mentor helping Indian B.Tech CSE AIML students prepare for internships.
Give practical, beginner-friendly, encouraging advice. Keep answers concise and actionable.
"""

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []

for message in st.session_state.chat_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Type your question here...")

if user_input:
    st.session_state.chat_messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                conversation_text = system_context + "\n\n"

                for message in st.session_state.chat_messages:
                    if message["role"] == "user":
                        conversation_text += "Student: " + message["content"] + "\n"
                    else:
                        conversation_text += "Mentor: " + message["content"] + "\n"

                conversation_text += "Student: " + user_input + "\nMentor:"

                response = client.models.generate_content(
                     model="gemini-2.5-flash",
                     contents=conversation_text
                )
                
                reply = response.text
            except Exception as error:
                reply = f"Something went wrong: {error}"

            st.markdown(reply)

    st.session_state.chat_messages.append({"role": "assistant", "content": reply})




