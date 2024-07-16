import streamlit as st 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
point = 0
if st.session_state.name=="NULL" and st.session_state.number=="NULL":
    "Please enter your information first"
else :
    st.title('this is a :rainbow[SIMPLE QUIZ]')

    answer1 = st.text_area('where do fish live?')
    answer2 = st.radio(
        'Which is heavier, 1kg gold or 1kg air?',
        ['gold', 'air', 'same', "I don't know"]
        )

    if st.button('submit'):
        if answer1=='PCroom' or answer1=='PC방':
            point+=50
        if answer2=='same':
            point+=50