import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="My AI",
    page_icon="🤖"
)

st.title("🤖 My AI")
st.caption("Tamil • English • Tanglish AI Assistant")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask me anything...")

if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.responses.create(
            model="gpt-5.6-mini",
            instructions="""
You are My AI, a helpful AI assistant.
Understand Tamil, English and Tanglish.
Reply in the same language used by the user.
Be friendly, clear and helpful.
""",
            input=prompt
        )

        answer = response.output_text
        st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })