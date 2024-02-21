import streamlit as st
from helpers_v2_k import turtle_with_speech_bubble, map_bg, click_m1_q1

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


# Quest Buttons and Button to open backpack
buttons = [
    {"label": "🏳️", "top": "77%", "left": "39%", "font-size": "3vw", "onclick": click_m1_q1},  # Button M1 Q1
    {"label": "🔒", "top": "68%", "left": "47%", "font-size": "3vw", "onclick": click_m1_q1},  # Button M1 expl
    {"label": "🔒", "top": "60%", "left": "54%", "font-size": "3vw", "onclick": click_m1_q1},  # Button M1 Q2
    {"label": "🔒", "top": "53%", "left": "48%", "font-size": "3vw", "onclick": click_m1_q1},  # Button M2 Q1
    {"label": "🔒", "top": "57%", "left": "38%", "font-size": "3vw", "onclick": click_m1_q1},  # Button M2 expl
    {"label": "🔒", "top": "47%", "left": "43%", "font-size": "3vw", "onclick": click_m1_q1},  # Button M2 Q2
    {"label": "🔒", "top": "49%", "left": "57%", "font-size": "3vw", "onclick": click_m1_q1},  # Button M3 Q1
    {"label": "🔒", "top": "33%", "left": "60%", "font-size": "3vw", "onclick": click_m1_q1},  # Button M3 expl
    # {"label": "🔒", "top": "70%", "left": "45%", "font-size": "3vw", "onclick": click_m1_q1},  # Button M3 Q2
]

col1, col2 = st.columns([0.2, 0.8])

with col1:
    turtle_with_speech_bubble(speech_turtle[0]['text'])

with col2:
    map_bg(buttons)

import streamlit as st

def st_tags(value: list,
            suggestions: list,
            label: str,
            text: str,
            maxtags: int,
            key=None) -> list:
    '''
    :param maxtags: Maximum number of tags allowed maxtags = -1 for unlimited entries
    :param suggestions: (List) List of possible suggestions (optional)
    :param label: (Str) Label of the Function
    :param text: (Str) Instructions for entry
    :param value: (List) Initial Value (optional)
    :param key: (Str)
        An optional string to use as the unique key for the widget.
        Assign a key so the component is not remount every time the script is rerun.
    :return: (List) Tags

    Note: usage also supports keywords = st_tags()
    '''

    col1, col2 = st.columns([2, 1])

    if suggestions:
        value = col1.multiselect(label=label,
                                 options=suggestions,
                                 default=value,
                                 key=key,
                                 help=text)
    else:
        value = col1.text_input(label=label,
                                value=' '.join(value),
                                key=key,
                                help=text)

    col2.write('This is some text displayed in the second column.')

    return value

