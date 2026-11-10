import streamlit as st

st.set_page_config(page_title="Multi-AI Council", layout="wide")
# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🏛️ Multi-AI Council Command Center")
st.sidebar.header("Configuration")
with st.sidebar:
        st.header("Chat Sessions")
        if st.button("🗑️ Clear Chat History"):
            st.session_state.messages = []
            st.rerun()
# API Keys input in sidebar
openai_key = st.sidebar.text_input("OpenAI API Key", type="password")
deepseek_key = st.sidebar.text_input("DeepSeek API Key", type="password")
gemini_key = st.sidebar.text_input("Gemini API Key", type="password")

prompt = st.text_area("Enter your master prompt for the Council:")

# 1. Render all past messages so they stay on screen when you scroll up
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 2. Capture new user prompt via the modern chat input box
if prompt := st.chat_input("Enter your master prompt for the Council:"):
    
    # Save and display your prompt immediately
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- YOUR EXISTING MULTI-AI API CALL LOGIC GOES HERE ---
    # (Make sure whatever variable holds your final combined AI response text is named `council_response`)
    council_response = f"Council response for: {prompt}"  # Replace this mock line with your actual API outputs
    # -------------------------------------------------------

    # Save and display the assistant's combined response
    st.session_state.messages.append({"role": "assistant", "content": council_response})
    with st.chat_message("assistant"):
        st.markdown(council_response)
    if not openai_key or not deepseek_key or not gemini_key:
        st.warning("Please enter all API keys in the sidebar first.")
    else:
        st.success("Council ready! Starting parallel generation...")
        import streamlit as st

# Example display structure for your council output:

    if not openai_key or not deepseek_key or not gemini_key:
        st.warning("Please enter all API keys in the sidebar first.")
    else:
     with st.spinner("Council is deliberating..."):
            # --- Put your API call logic here ---
            # openai_response = ...
            # deepseek_response = ...
            # gemini_response = ...

            # --- Display Outputs ---
            
            
            # Example for displaying OpenAI
            # st.markdown("### OpenAI")
            # st.write(openai_response)
            
            # Example for displaying DeepSeek
            # st.markdown("### DeepSeek")
            # st.write(deepseek_response)
            
            # Example for displaying Gemini
            # st.markdown("### Gemini")
            # st.write(gemini_response)
            