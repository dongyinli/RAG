import streamlit as st
import time

from rag import RagService
import config_data as config


# Page title
st.title("AI Customer Support")

# Divider
st.divider()

# Store chat history in session state
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "assistant",
            "content": "Hello! How can I help you today?"
        }
    ]

# Store RAG service instance in session state
if "rag_service" not in st.session_state:
    st.session_state["rag_service"] = RagService()

# Display chat history
for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

# User input box
user_prompt = st.chat_input()

if user_prompt:
    # Display user message
    st.chat_message("user").write(user_prompt)
    st.session_state["messages"].append(
        {"role": "user", "content": user_prompt}
    )

    response_chunks = []

    with st.spinner("AI is thinking..."):
        # Direct output example
        # response = st.session_state["rag_service"].chain.invoke(
        #     {"input": user_prompt},
        #     config.session_config
        # )
        #
        # st.chat_message("assistant").write(response)
        # st.session_state["messages"].append(
        #     {"role": "assistant", "content": response}
        # )

        # Streaming output
        response_stream = st.session_state["rag_service"].chain.stream(
            {"input": user_prompt},
            config.session_config
        )

        def capture_stream(generator, cache):
            for chunk in generator:
                cache.append(chunk)
                yield chunk

        st.chat_message("assistant").write_stream(
            capture_stream(response_stream, response_chunks)
        )

        st.session_state["messages"].append(
            {
                "role": "assistant",
                "content": "".join(response_chunks)
            }
        )
