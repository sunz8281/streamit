import streamlit as st
import time

if 'name' not in st.session_state:
    st.session_state.name = "NULL"
if 'number' not in st.session_state:
    st.session_state.number = "NULL"

md = "Hello/o/o/o/o/o/o/o/o/o/o/o/o/o/o/! :balloon:"

def stream_data():
    for word in md.split("/"):
        yield word + ""
        time.sleep(0.05)


st.title(":eyes: :rainbow[Application form]")
st.write_stream(stream_data)
name = st.text_area("What's your name?")
number = st.text_input("What is your school number?")
if st.button('submit'):
    st.session_state.name = name
    st.session_state.number = number