import streamlit as st
from helpers import turtle_with_speech_bubble, map_bg

st.set_page_config(
    page_title="PIErats - Productivity Island Expedition",
    page_icon="🐢"
)

# creates a dictionary in a list to fill the speech bubble
speech_turtle = [
    {"text": "Hey Sailor! Looks like you and your little brother stranded on a deserted island. Unfortunately, "
             "your boat has broken down and you need new equipment. As you explore the individual quests, "
             "you will find new materials and learn new things in order to survive and ultimately escape from the "
             "island. Let's get started and begin with the first quest!"
     }
]

# call the function to display the turtle, speech bubble and the first text inside the speech bubble
turtle_with_speech_bubble(speech_turtle[0]['text'])


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
    # {"label": "🔒", "top": "70%", "left": "45%", "font-size": "45px"},  # Button M3 Q2
]

# call the function to display the map as the background image and insert the buttons on top of it
map_bg(buttons)

