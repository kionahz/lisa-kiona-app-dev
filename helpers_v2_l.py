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
            <div style="position: fixed; top: 5%; left: 5%">
                <img src="{blue_bg_image_url}" alt="Map" width="50%"> </div>
            <div style="position: fixed; bottom: 10%; left: 5%;"> 
                <img src="{turtle_image_url}" alt="Turtle" width="10%"> </div>
            <div style="position: fixed; top:30%; left:5%">
                <img src="{speech_bubble_image_url}" alt="Speech bubble" width="20%"> </div>
            <div style="position: fixed; top: 60%; left: 5%; font-size: 20px; text-align: left; max-width: 
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
            bottom: 5%;
            right: 5%;
            font-size: 2vw;
            transform: translate(-50%, -50%);
            padding: 1%;
            background-color: non
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        """

    # Display the image with dynamically created buttons
    st.markdown(
        f"""
        <div style="position: fixed; top: 9%">
            <img src="{bg_image_url}" alt="Map" width="104%"> 
        """
        + "".join([
            f'<button style="position: absolute; top: {button["top"]}; left: {button["left"]}; font-size: {button["font-size"]}; transform: translate(-50%, -50%); padding: 1%;">{button["label"]}</button>'
            for button in buttons])
        + f"""
        </div>
        <button style="position: fixed; top: 10%; right: 5%; font-size: 4vw; transform: translate(-50%, -50%); padding:1%;"> 🏠</button>
        <div style="position:fixed; bottom: 5%; right: 5%;">
            <img src="{backpack_image_url}" alt="Backpack" width="20%"> </div> 
            <button style="{inventory_button_style}"> Inventory </button> 
        """,
        unsafe_allow_html=True
    )

