import streamlit  as st
import google.generativeai as genai

st.title("welcome to my bot")
genai.configure(api_key="AIzaSyCGIakY3kqIepjCbHSsVNjsCph7l8p73ss")

text=st.text_input('enter your question')

model=genai.GenerativeModel('gemini-pro')
chat=model.start_chat(history=[])
if st.button("Click me"):
    response= chat.send_message(text)
    st.write(response.text)