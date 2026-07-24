# KnowledgeBase-RAG-LLM-System

A local knowledge base upload and RAG-powered question answering project built with Streamlit.

Suitable as an introductory hands-on project for learning local knowledge base QA systems and Retrieval-Augmented Generation (RAG).

## Features

* Upload `.txt` files through the web interface, automatically split the documents, and store them in a Chroma vector database.
* Ask questions in a chat-style interface, with answers enhanced by retrieval from the knowledge base (RAG).
* Support for conversation history viewing and streaming Chain-of-Thought-style output.
* Tech Stack: Python / Streamlit / LangChain / Chroma / Embeddings / Qwen ChatModel

---

## System Overview

### 1) Knowledge Base Management (Upload)

- Upload text files through the Streamlit web interface
- Automatically read and process document content
- Split documents using `RecursiveCharacterTextSplitter`
- Store document embeddings in a persistent local Chroma vector database
- Prevent duplicate uploads using **MD5 hash-based deduplication**

### 2) RAG-Powered Chat Assistant

- Interactive chat interface built with Streamlit
- Display conversation history using `session_state`
- LangChain pipeline: `Retrieval -> Prompt -> LLM -> Output`
- Support real-time streaming responses
- Persist chat history using `FileChatMessageHistory`