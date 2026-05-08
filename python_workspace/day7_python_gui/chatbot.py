import streamlit as st

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 11-1
prompt = st.chat_input("질문 입력")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 11-2
    with st.chat_message("user"):
        st.write(prompt)

    response = f"당신이 말한 건: {prompt}"

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.write(response)