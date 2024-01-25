import streamlit as st
import base64


# function to display the turtle with an empty speech bubble
def turtle_with_speech_bubble(text):
    blue_bg_image = open("AD_Pictures/blue_bg.png", "rb").read()  # reads the blue square bg image
    turtle_image = open("AD_Pictures/turtle.png", "rb").read()  # reads the image of Shelly
    speech_bubble_image = open("AD_Pictures/speech_bubble.png", "rb").read()  # reads the speech bubble image

    # Convert the images to base64, so it can be embedded with HTML and CSS code
    blue_bg_image_base64 = base64.b64encode(blue_bg_image).decode('utf-8')
    blue_bg_image_url = f"data:image/png;base64,{blue_bg_image_base64}"
    turtle_image_base64 = base64.b64encode(turtle_image).decode('utf-8')
    turtle_image_url = f"data:image/png;base64, {turtle_image_base64}"
    speech_bubble_image_base64 = base64.b64encode(speech_bubble_image).decode('utf-8')
    speech_bubble_image_url = f"data:image/png;base64, {speech_bubble_image_base64}"

    st.markdown(
        f""" 
            <div style="position: fixed; top: 80px; left: 0px">
                <img src="{blue_bg_image_url}" alt="Map" width="1800"> </div>
            <div style="position: fixed; bottom: 40px; left: 10px;"> 
                <img src="{turtle_image_url}" alt="Turtle" width="300"> </div>
            <div style="position: fixed; top:90px; left:10px">
                <img src="{speech_bubble_image_url}" alt="Speech bubble" width="500"> </div>
            <div style="position: fixed; top: 105px; left: 10px; font-size: 20px; text-align: left; max-width: 
            500px; padding: 50px; color: black "> {text} 
            </div> """,
        unsafe_allow_html=True
    )


# function to display the map as the background image
def map_bg(buttons):

    bg_image = open("AD_Pictures/island.png", "rb").read()  # reads the bg map
    backpack_image = open("AD_Pictures/backpack.png", "rb").read()  # reads the image of the backpack

    # Convert the images to base64, so it can be embedded with HTML and CSS code
    bg_image_base64 = base64.b64encode(bg_image).decode('utf-8')
    bg_image_url = f"data:image/png;base64,{bg_image_base64}"
    backpack_image_base64 = base64.b64encode(backpack_image).decode('utf-8')
    backpack_image_url = f"data:image/png;base64, {backpack_image_base64}"

    inventory_button_style = """
            position: fixed;
            bottom: 30px;
            right: 30px;
            font-size: 25px;
            transform: translate(-50%, -50%);
            padding: 5px;
            background-color: non
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        """

    # Display the image with dynamically created buttons
    st.markdown(
        f"""
        <div style="position: fixed; top: 90px">
            <img src="{bg_image_url}" alt="Map" width="1200"> 
        """
        + "".join([
            f'<button style="position: absolute; top: {button["top"]}; left: {button["left"]}; font-size: {button["font-size"]}; transform: translate(-50%, -50%); padding: 5px;">{button["label"]}</button>'
            for button in buttons])
        + f"""
        </div>
        <button style="position: fixed; top: 140px; right: 5px; font-size: 55px; transform: translate(-50%, -50%); padding:5px;"> 🏠</button>
        <div style="position:fixed; bottom: 10px; right: 10px;">
            <img src="{backpack_image_url}" alt="Backpack" width="230"> </div> 
            <button style="{inventory_button_style}"> Inventory </button> 
        """,
        unsafe_allow_html=True
    )

