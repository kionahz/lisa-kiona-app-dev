import streamlit as st
from gpt_helper import st_tags
from helpers_v2_k import turtle_with_speech_bubble, eisenhower_bg

st.set_page_config(
    page_title="PIErats - Productivity Island Expedition",
    page_icon="🐢",
    layout="wide"
)
eisenhower_bg()

import streamlit as st

# Create a 3-column layout
col1, col2, col3 = st.columns(3)

# Add input boxes to the columns
with col1:
    st.text_input('Input 1')

with col2:
    st.text_input('Input 2')

with col3:
    st.text_input('Input 3')

# Add custom HTML and CSS to style the layout
st.markdown(
    """
    <style>
    .st-bw {
        display: flex;
        flex-direction: row;
        justify-content: space-around;
    }
    </style>
    """
    , unsafe_allow_html=True
)




