import streamlit as st

st.set_page_config(page_title="Multi-AI Council", layout="wide")

st.title("🏛️ Multi-AI Council Command Center")
st.sidebar.header("Configuration")

# API Keys input in sidebar
openai_key = st.sidebar.text_input("OpenAI API Key", type="password")
deepseek_key = st.sidebar.text_input("DeepSeek API Key", type="password")
gemini_key = st.sidebar.text_input("Gemini API Key", type="password")

prompt = st.text_area("Enter your master prompt for the Council:")

if st.button("🚀 Launch Deliberation"):
    if not openai_key or not deepseek_key or not gemini_key:
        st.warning("Please enter all API keys in the sidebar first.")
    else:
        st.success("Council ready! Starting parallel generation...")
        