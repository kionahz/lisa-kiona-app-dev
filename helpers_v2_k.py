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
            <div style="position: fixed; top: 0%; left: 0%">
                <img src="{blue_bg_image_url}" alt="Map" width="200%"> </div>
            <div style="position: fixed; bottom: 3%; left: 1%;"> 
                <img src="{turtle_image_url}" alt="Turtle" width="30%"> </div>
            <div style="position: fixed; top: 5%; left: 0%;">
                <img src="{speech_bubble_image_url}" alt="Speech bubble" width="33%"> </div>
            <div style="position: fixed; top: 8.5%; left: 0.5%; font-size: 1.5vw; text-align: left; max-width: 
            32%; padding: 1%; color: black "> {text} 
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
            <img src="{bg_image_url}" alt="Map" width="110%"> 
        """
        + "".join([
            f'<button style="position: absolute; top: {button["top"]}; left: {button["left"]}; '
            f'font-size: {button["font-size"]}; transform: translate(-50%, -50%); '
            f'padding: 1%;" onclick="{button["onclick"]}">{button["label"]}</button>'
            for button in buttons])
        + f"""
        </div>
        <button style="position: fixed; top: 10%; right: 5%; font-size: 4vw; transform: translate(-50%, -50%); padding:1%;"> 🏠</button>
        <div style="position: fixed; bottom: 5%; left: 85%">
            <img src="{backpack_image_url}" alt="Backpack" width="100%"> </div> 
            <button style="{inventory_button_style}"> Inventory </button> 
        """,
        unsafe_allow_html=True
    )


def click_m1_q1():
    print('Button is clicked')


    # onclick="{button["execution"]}" command code to execute a button with html
    # -> we have to figure out how to open further pages with click on a button

def eisenhower_bg():
    old_page_image = open("AD_Pictures/em_empty.png", "rb").read()  # reads the image of the backpack

    # Convert the images to base64, so it can be embedded with HTML and CSS code
    old_page_image_base64 = base64.b64encode(old_page_image).decode('utf-8')
    old_page_image_url = f"data:image/png;base64,{old_page_image_base64}"

    st.markdown(
       f"""
        <div style="position: fixed; top: 12%; left: 25%;">
            <img src="{old_page_image_url}" alt="Old Page" width="110%"></div>
        <button style="position: fixed; top: 14%; right: 0.5%; font-size: 4vw; transform: translate(-50%, -50%); padding: 1%;" >🏠</button>
        """,
       unsafe_allow_html=True
    )
