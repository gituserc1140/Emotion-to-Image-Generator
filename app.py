import streamlit as st
import replicate

st.title("Emotion to Image Generator")

# Initialize session state for API token
if 'api_token' not in st.session_state:
    st.session_state.api_token = ''

# Sidebar for API token input
with st.sidebar:
    st.session_state.api_token = st.text_input("Replicate API Token", type="password")

# Emotion input
emotion = st.text_input("Enter an emotion (e.g., happy, sad, angry):")

if st.button("Generate Image") and st.session_state.api_token and emotion:
    try:
        # Set Replicate API token
        replicate.Client(api_token=st.session_state.api_token)
        
        # Generate image using SDXL model
        output = replicate.run(
            "stability-ai/sdxl:latest",
            input={"prompt": f"An image representing {emotion} emotion"}
        )
        
        # Display generated image
        st.image(output[0], caption=f"Generated Image for {emotion} Emotion")
    except Exception as e:
        st.error(f"Error generating image: {e}")

