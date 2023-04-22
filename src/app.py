import streamlit as st
import requests




st.title('GPTと会話をしよう！！')

title = st.text_input('Movie title', 'Life of Brian')


def insert():
    return st.write("追加")

if st.button('送信'):
    st.write(title)
    st.write("こんにちは")