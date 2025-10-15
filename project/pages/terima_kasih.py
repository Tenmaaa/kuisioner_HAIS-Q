import streamlit as st

st.title("Terima Kasih telah mengisi, jawaban anda sangat penting untuk penelitian ini :)")
for key in st.session_state.keys():
            del st.session_state[key]