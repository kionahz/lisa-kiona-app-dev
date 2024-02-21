import base64
import streamlit as st

speech_turtle = [
    {"text_introduction": "Hey Sailor! Looks like you and your little brother stranded on a deserted island. "
                          "Unfortunately, your boat has broken down and you need new equipment. As you explore the "
                          "individual quests, you will find new materials and learn new things in order to survive "
                          "and ultimately escape from the island. Let's get started and begin with the first quest!"},

    {"text_m1_q1": "There are now a few things you need to do to ensure your survival. You have several possible "
                   "tasks as options that you can do now. But you can't do them all at once, so you have to "
                   "prioritize. Which task do you start with and which ones can you do later? Sort the tasks into an "
                   "order. Start with the most important task at the top and end with the least important task at the "
                   "bottom."}
]

def update_text(texts, blue_bg_image_url, turtle_image_url, speech_bubble_image_url):
    st.markdown(
        f""" 
            <div style="position: fixed; top: 0%; left: 0%">
                <img src="{blue_bg_image_url}" alt="Map" width="200%"> </div>
            <div style="position: fixed; bottom: 3%; left: 1%;"> 
                <img src="{turtle_image_url}" alt="Turtle" width="30%"> </div>
            <div style="position: fixed; top: 5%; left: 0%;">
                <img src="{speech_bubble_image_url}" alt="Speech bubble" width="33%"> </div>
            <div style="position: fixed; top: 8.5%; left: 0.5%; font-size: 1.5vw; text-align: left; max-width: 
            32%; padding: 1%; color: black "> {texts} 
            </div> """,
        unsafe_allow_html=True
    )


def turtle_with_speech_bubble(texts):
    if 'current_text_index' not in st.session_state:
        st.session_state.current_text_index = 0

    blue_bg_image = open("AD_Pictures/blue_bg.png", "rb").read()
    turtle_image = open("AD_Pictures/turtle.png", "rb").read()
    speech_bubble_image = open("AD_Pictures/speech_bubble.png", "rb").read()

    # Convert the images to base64, so they can be embedded with HTML and CSS code
    blue_bg_image_base64 = base64.b64encode(blue_bg_image).decode('utf-8')
    turtle_image_base64 = base64.b64encode(turtle_image).decode('utf-8')
    speech_bubble_image_base64 = base64.b64encode(speech_bubble_image).decode('utf-8')

    blue_bg_image_url = f"data:image/png;base64,{blue_bg_image_base64}"
    turtle_image_url = f"data:image/png;base64,{turtle_image_base64}"
    speech_bubble_image_url = f"data:image/png;base64,{speech_bubble_image_base64}"

    update_text(texts[st.session_state.current_text_index], blue_bg_image_url, turtle_image_url, speech_bubble_image_url)

    if st.session_state.current_text_index < len(texts) - 1:
        if st.button("Next"):
            st.session_state.current_text_index += 1


# call the function to display the turtle, speech bubble and the first text inside the speech bubble
turtle_with_speech_bubble([speech_turtle[0]['text_introduction'], speech_turtle[1]['text_m1_q1']])
