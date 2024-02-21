import streamlit as st

st.set_page_config(
    page_title="PIErats - Productivity Island Expedition",
    page_icon="🐢",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "This app generates scripts for data clean rooms!"
    }
)

# Set up main page
col1, col2 = st.columns((6, 1))
col1.title("PIErats - Productivity Island Expedition")
col2.image("AD_Pictures/logo.png", width=120)
st.sidebar.image("AD_Pictures/turtle.png")
action = st.sidebar.radio("What action would you like to take?", ("Initial Deployment 🐻‍❄",
                                                                  "Add Add'l Consumer 🐧️",
                                                                  "Add Add'l Provider ☃️",
                                                                  "Uninstall 💧"))
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #29bdbc;
    }
</style>
""", unsafe_allow_html=True)

