import streamlit as st
import openai

openai.api_key = st.secrets["my_other_secrets"]["API_KEY"]

# @see: https://qiita.com/suzuki_sh/items/fb7a21426043d8520dbe
def stream_write(chunks, key=None):
    result_area = st.empty()
    text = ''
    for chunk in chunks:
        next: str = chunk['choices'][0]['delta'].get('content', '') 
        text += next
        if "。" in next:
            text += "\n"
        result_area.write(text, key=key)
    return text

@st.cache_data
def cached_chat(messages):
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        stream=True,
    )
    text = stream_write(completion, key=f'output_{messages}')
    return text

messages = []
chat_widget = st.empty()


while True:
    with chat_widget.container():
        for message in messages:
            st.write(message['content'])
        input_text = st.text_input('AIに質問する', key=f'input_{messages}',max_chars=100)
        if len(input_text) == 0:
            st.stop()
        messages.append({"role": "user", "content": input_text})
        #text = cached_chat(messages)
        #messages.append({"role": "assistant", "content": text})