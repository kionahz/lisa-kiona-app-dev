import streamlit as st
import base64

st.set_page_config(
    page_title="PIErats - Productivity Island Expedition",
    page_icon="🐢"
)

bg_image_map = "AD_Pictures/island_blurr.png"
blue_bg = "AD_Pictures/blue_bg.png"
open_backpack_bg = "AD_Pictures/open_backpack.png"
turtle_character_image = "AD_Pictures/turtle.png"
speechbubble_img = "AD_Pictures/speech_bubble.png"
speech_turtle = [
    {"text": "Let's check which items you have earned so far!"
     }
]


def turtle_speechbubble(speech_turtle, blue_bg, speechbubble_img):
    blue_bg_image = open(blue_bg, "rb").read()

    speechbubble_image = open(speechbubble_img, "rb").read()


    # Convert the image to base64
    blue_bg_image_base64 = base64.b64encode(blue_bg_image).decode('utf-8')
    blue_bg_image_url = f"data:image/png;base64,{blue_bg_image_base64}"

    speechbubble_image_base64 = base64.b64encode(speechbubble_image).decode('utf-8')
    speechbubble_image_url = f"data:image/png;base64, {speechbubble_image_base64}"

    st.markdown(
        f""" 
            <div style="position: fixed; top: 80px; left: 0px">
                <img src="{blue_bg_image_url}" alt="Map" width="1800"> </div>
            <div style="position: fixed; top:90px; left:10px">
                <img src="{speechbubble_image_url}" alt="Speechbubble" width="500"> </div>
            <div style="position: fixed; top: 105px; left: 10px; font-size: 30px; text-align: left; max-width: 
            500px; padding: 50px; color: black "> {speech_turtle[0]["text"]} 
            <button style="position: fixed; bottom: 10px; left: 450px; font-size: 50px; transform: translate(-50%, -50%); 
            padding:5px;">🏠</button> </div> """,
        unsafe_allow_html=True
    )

    if st.button("Home"):
        st.switch_page("Pierats_v4_k.py")


turtle_speechbubble(speech_turtle, blue_bg, speechbubble_img)

def open_backpack_page(open_backpack_bg, turtle_character_image):
    open_backpack_image = open(open_backpack_bg, "rb").read()

    turtle_image = open(turtle_character_image, "rb").read()

    open_backpack_image_base64 = base64.b64encode(open_backpack_image).decode('utf-8')
    open_backpack_image_url = f"data:image/png;base64, {open_backpack_image_base64}"


    turtle_image_base64 = base64.b64encode(turtle_image).decode('utf-8')
    turtle_image_url = f"data:image/png;base64, {turtle_image_base64}"

    bg_image = open(bg_image_map, "rb").read()

    # Convert the image to base64
    bg_image_base64 = base64.b64encode(bg_image).decode('utf-8')
    bg_image_url = f"data:image/png;base64,{bg_image_base64}"

    st.markdown(
        f"""
        <div style="position: fixed; top: 80px; left: 430px">
            <img src="{bg_image_url}" alt="Map" width="1300"> 
        </div>
        <div style="position: fixed; top: 15px; right: 70px">
            <img src="{open_backpack_image_url}" alt="Map" width="900"> 
        </div>
        <div style="position: fixed; bottom: 40px; left: 10px;">
            <img src="{turtle_image_url}" alt="Turtle" width="300">
        </div>
        """
        ,
        unsafe_allow_html=True
    )


open_backpack_page(open_backpack_bg, turtle_character_image)
