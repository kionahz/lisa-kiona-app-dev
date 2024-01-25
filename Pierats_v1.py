import streamlit as st
import base64


st.set_page_config(
    page_title="PIErats - Productivity Island Expedition",
    page_icon="🐢"
)

# Variables
bg_image_map = "AD_Pictures/island.png"  # Directory for island image
blue_bg = "AD_Pictures/blue_bg.png"  # Directory for blue square as overall bg
backpack_icon_image = "AD_Pictures/backpack.png"  # Directory for the backpack image
turtle_character_image = "AD_Pictures/turtle.png"  # Directory for Shelly image
speechbubble_img = "AD_Pictures/speech_bubble.png"  # Directory for image of speech bubble
# creates a dictionary in a list to fill the speech bubble
speech_turtle = [
    {"text": "Hey Sailor! Looks like you and your little brother stranded on a deserted island. Unfortunately, "
             "your boat has broken down and you need new equipment. As you explore the individual quests, "
             "you will find new materials and learn new things in order to survive and ultimately escape from the "
             "island. Let's get started and begin with the first quest!"
     }
]


def turtle_speechbubble(speech_turtle, blue_bg, speechbubble_img):  # calls variables
    blue_bg_image = open(blue_bg, "rb").read()  # reads the blue square bg image
    speechbubble_image = open(speechbubble_img, "rb").read()  # reads the speech bubble image

    # Convert the images to base64, so it can be embedded with HTML and CSS code
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
        <div style="position: fixed; top: 105px; left: 10px; font-size: 20px; text-align: left; max-width: 
        500px; padding: 50px; color: black "> {speech_turtle[0]["text"]} 
        </div> """,
        unsafe_allow_html=True
    )


turtle_speechbubble(speech_turtle, blue_bg, speechbubble_img)


# Function to display the play buttons as an overlay on the map
def map_q1(bg_image_map, turtle_character_image, buttons, backpack_icon_image):

    bg_image = open(bg_image_map, "rb").read()  # reads the bg map
    turtle_image = open(turtle_character_image, "rb").read()  # reads the image of Shelly
    backpack_image = open(backpack_icon_image, "rb").read()  # reads the image of the backpack

    # Convert the images to base64, so it can be embedded with HTML and CSS code
    bg_image_base64 = base64.b64encode(bg_image).decode('utf-8')
    bg_image_url = f"data:image/png;base64,{bg_image_base64}"
    turtle_image_base64 = base64.b64encode(turtle_image).decode('utf-8')
    turtle_image_url = f"data:image/png;base64, {turtle_image_base64}"
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
            <div style="position: fixed; bottom: 40px; left: 10px;"> <img src="{turtle_image_url}" alt="Turtle" 
            width="300">
        </div>
        """,
        unsafe_allow_html=True
    )


# onclick="{button["execution"]}" command code to execute a button with html
# -> we have to figure out how to open further pages with click on a button

# Quest Buttons and Button to open backpack
buttons = [
    {"label": "🏳️", "top": "77%", "left": "39%", "font-size": "45px"},  # Button M1 Q1
    {"label": "🔒", "top": "68%", "left": "47%", "font-size": "45px"},  # Button M1 expl
    {"label": "🔒", "top": "60%", "left": "54%", "font-size": "45px"},  # Button M1 Q2
    {"label": "🔒", "top": "53%", "left": "48%", "font-size": "45px"},  # Button M2 Q1
    {"label": "🔒", "top": "57%", "left": "38%", "font-size": "45px"},  # Button M2 expl
    {"label": "🔒", "top": "47%", "left": "43%", "font-size": "45px"},  # Button M2 Q2
    {"label": "🔒", "top": "49%", "left": "57%", "font-size": "45px"},  # Button M3 Q1
    {"label": "🔒", "top": "33%", "left": "60%", "font-size": "45px"},  # Button M3 expl
    #{"label": "🔒", "top": "70%", "left": "45%", "font-size": "45px"},  # Button M3 Q2
]

# Call the function with the parameters
map_q1(bg_image_map, turtle_character_image, buttons, backpack_icon_image)