import streamlit as st
import os
import threading
import time

# wait time to close page and open a new one.
wait_second = 3.8


# thread for closing page
def threadFunc():
    time.sleep(wait_second)
    os.system('taskkill /F /FI "WindowTitle eq Pierats - Productivity Island Expedition"')


if 'page' in st.experimental_get_query_params():
    if st.experimental_get_query_params()['page'][0] == 'open_backpack':
        os.system('streamlit run open_backpack.py')

if st.button('test'):
    th = threading.Thread(target=threadFunc)
    th.start()
    os.system('streamlit run pierats.py')
    th.join()
