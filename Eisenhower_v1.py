import streamlit as st
from helpers_v2_k import turtle_with_speech_bubble, eisenhower_bg


speech_turtle = [
    {"text": "Hey Sailor! Looks like you and your little brother stranded on a deserted island. Unfortunately, "
             "your boat has broken down and you need new equipment. As you explore the individual quests, "
             "you will find new materials and learn new things in order to survive and ultimately escape from the "
             "island. Let's get started and begin with the first quest!"},
    {
        "text": "There are now a few things you need to do to ensure your survival. You have several possible tasks as options "
                "that you can do now. But you can't do them all at once, so you have to prioritize. Which task do you start "
                "with and which ones can you do later? Sort the tasks into an order. Start with the most important task at the "
                "top and end with the least important task at the bottom."
        }
]

turtle_with_speech_bubble(speech_turtle[1]['text'])

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


list = st_tags(
    label='# Enter Keywords:',
    text='Press enter to add more',
    value=['Zero', 'One', 'Two'],
    suggestions=['five', 'six', 'seven',
                 'eight', 'nine', 'three',
                 'eleven', 'ten', 'four'],
    maxtags=4,
    key='1')



eisenhower_bg()



